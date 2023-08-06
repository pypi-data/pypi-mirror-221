# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['stability_matrix_tools',
 'stability_matrix_tools.models',
 'stability_matrix_tools.utils']

package_data = \
{'': ['*']}

install_requires = \
['b2sdk>=1.21.0,<2.0.0',
 'blake3>=0.3.3,<0.4.0',
 'cryptography>=41.0.1,<42.0.0',
 'httpx>=0.24.1,<0.25.0',
 'keyring>=24.2.0,<25.0.0',
 'pydantic[dotenv]>=2.0.1,<3.0.0',
 'pyperclip>=1.8.2,<2.0.0',
 'python-dotenv>=1.0.0,<2.0.0',
 'semver>=3.0.1,<4.0.0',
 'typer[all]>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['sm-tools = stability_matrix_tools.main:app']}

setup_kwargs = {
    'name': 'stability-matrix-tools',
    'version': '0.2.1',
    'description': '',
    'long_description': '# sm-tools\n Stability Matrix development tools\n',
    'author': 'Ionite',
    'author_email': 'dev@ionite.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
