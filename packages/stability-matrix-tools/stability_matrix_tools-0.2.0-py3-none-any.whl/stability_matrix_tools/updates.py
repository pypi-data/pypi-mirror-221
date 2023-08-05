"""Manages automatic updates"""
import base64
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from typing_extensions import Annotated
from urllib.parse import urljoin

from httpx import HTTPStatusError

from stability_matrix_tools.models.update_info import UpdateInfo, UpdateCollection, UpdateType
from stability_matrix_tools.models.settings import env
from stability_matrix_tools.utils import signing
from stability_matrix_tools.utils.stream_hash import blake3_hash_file

import typer
import httpx
from rich import print as cp

from stability_matrix_tools.utils.cf_cache import cache_purge
from stability_matrix_tools.utils.progress import RichProgressListener
from stability_matrix_tools.utils.uploader import Uploader

app = typer.Typer()


def info_sign_data(info: UpdateInfo) -> str:
    """Returns the data to be signed"""
    return ";".join(
        [
            info.version,
            info.release_date,
            info.channel,
            info.type,
            info.url,
            info.changelog,
            info.hash_blake3,
        ]
    )


def validate_platform(platform: str) -> str:
    if platform not in ("win-x64", "linux-x64"):
        raise ValueError(f"Unknown platform: {platform!r}")
    return platform


# noinspection PyShadowingBuiltins
def sign_update(
        version: str,
        release_date: datetime,
        channel: str,
        type: UpdateType,
        url: str,
        changelog: str,
        hash_blake3: str,
) -> str:
    """
    Signs an update info.
    Returns base64 encoded signature.
    """
    # Signature is of the semicolon separated values:
    # version, releaseDate, channel, type, url, changelog, hash_blake3"
    data = ";".join(
        [
            version,
            release_date.replace(tzinfo=timezone.utc).isoformat(),
            channel,
            str(type.value),
            url,
            changelog,
            hash_blake3,
        ]
    )
    cp(f"Data to sign: {data!r}")

    private_key = signing.get_private_key_keyring()
    if not private_key:
        raise RuntimeError("Private key not found.")

    signature = private_key.sign(data.encode("utf-8"))
    return base64.b64encode(signature).decode("utf-8")


@app.command()
def publish(
    platform: Annotated[str, typer.Option("--platform", "-p")],
    version: Annotated[str, typer.Option("--version", "-v")],
    url: Annotated[str, typer.Option("--url", "-u")],
    changelog: Annotated[str, typer.Option("--changelog")],
    channel: Annotated[str, typer.Option("--channel")] = "stable",
    update_type: Annotated[UpdateType, typer.Option("--type")] = 1,
    b2_path: Annotated[str, typer.Option("--b2-path")] = "update-v2.json",
    confirm: Annotated[bool, typer.Option("--yes", "-y")] = False,
):
    """Publishes an update"""
    validate_platform(platform)

    # Like publish_manual, but download the file to get blake3 hash

    # Get file name from last part of url
    file_name = url.split("/")[-1]
    cp(f"Downloading {file_name}...")

    with TemporaryDirectory() as temp_dir:
        temp_file = Path(temp_dir, file_name)
        with httpx.stream("GET", url, follow_redirects=True) as r:
            r.raise_for_status()
            with temp_file.open("wb") as f:
                for chunk in r.iter_bytes():
                    f.write(chunk)

        hash_blake3 = blake3_hash_file(temp_file)
        cp(f"Blake3 Hash: {hash_blake3}")

    # Call manual
    publish_manual(
        platform=platform,
        version=version,
        url=url,
        changelog=changelog,
        hash_blake3=hash_blake3,
        channel=channel,
        update_type=update_type,
        b2_path=b2_path,
        confirm=confirm,
    )


@app.command()
def publish_manual(
    platform: str,
    version: str,
    url: str,
    changelog: str,
    hash_blake3: str,
    channel: str = "stable",
    update_type: UpdateType = 1,
    b2_path: str = "update-v2.json",
    confirm: bool = typer.Option(True, "--yes", "-y"),
):
    """Publishes an update"""

    validate_platform(platform)

    # Fetch current json first to update a single platform
    cp("Fetching current manifest...")

    current_collection: UpdateCollection | None = None

    try:
        url = urljoin(env.cdn_root, b2_path)
        response = httpx.get(url, headers={"Cache-Control": "no-cache"})
        response.raise_for_status()

        cp(f"✅  {url!r} -> ({response.status_code})")

        current_collection = UpdateCollection.model_validate_json(response.text)
    except HTTPStatusError as e:
        cp(f"Skipped current manifest ({e.response.status_code})")

    if current_collection is not None and current_collection.win_x64 is not None:
        cp(f"Current win-x64: {current_collection.win_x64.version}")
    if current_collection is not None and current_collection.linux_x64 is not None:
        cp(f"Current linux-x64: {current_collection.linux_x64.version}")
    if current_collection is None:
        # Create empty collection
        current_collection = UpdateCollection()

    release_date = datetime.utcnow()
    cp(f"New Release Date: {release_date}")

    # Make signature
    cp("Signing update...")
    signature = sign_update(
        version=version,
        release_date=release_date,
        channel=channel,
        type=update_type,
        url=url,
        changelog=changelog,
        hash_blake3=hash_blake3,
    )
    cp(f"Created Signature: {signature!r}")

    info = UpdateInfo(
        version=version,
        releaseDate=release_date,
        channel=channel,
        url=url,
        changelog=changelog,
        hashBlake3=hash_blake3,
        signature=signature,
        type=update_type,
    )

    # Update collection
    if platform == "win-x64":
        current_collection.win_x64 = info
    elif platform == "linux-x64":
        current_collection.linux_x64 = info
    else:
        raise ValueError(f"Unknown platform: {platform!r}")

    # Print and ask for confirmation
    json = current_collection.model_dump_json(indent=4, by_alias=True)
    cp(f"Update Info JSON: {json}")

    if not confirm and not typer.confirm("Publish update?"):
        raise typer.Abort()

    # Save json to a temporary file
    with TemporaryDirectory() as temp_dir:
        temp_file = Path(temp_dir, "update.json")
        temp_file.write_text(json)

        # Upload file
        cp("Uploading...")
        uploader = Uploader(env.b2_api_id, env.b2_api_key, env.b2_bucket_name)
        uploader.upload(temp_file, b2_path)

        with RichProgressListener("Uploading...", transient=True) as pbar:
            uploader.upload(temp_file, b2_path, pbar)

    typer.echo("Updating Cloudflare cache...")
    cache_purge(urljoin(env.cdn_root, b2_path))

    result = urljoin(env.cdn_root, b2_path)
    typer.echo(f"✅  Uploaded at: {result!r}")


@app.command()
def check(b2_path: str = "update-v2.json"):
    """Checks for updates"""

    cp(f"Checking for updates...")

    url = urljoin(env.cdn_root, b2_path)
    # Use a cache-control 0 header to ensure we get the latest version
    res = httpx.get(url, headers={"Cache-Control": "no-cache"})
    try:
        res.raise_for_status()
    except HTTPStatusError as e:
        cp(f"❌  {url!r} -> ({e.response.status_code})")
        return

    cp(f"✅  {url!r} -> ({res.status_code})")
    cp(res.json())

    updates = UpdateInfo.model_validate_json(res.text)
    cp(updates)
