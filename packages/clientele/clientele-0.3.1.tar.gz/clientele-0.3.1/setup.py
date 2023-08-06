# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src', 'src.generators', 'src.template']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'httpx>=0.24.1,<0.25.0',
 'openapi-core==0.18.0',
 'pydantic>=2.0.3,<3.0.0',
 'pyyaml>=6.0.1,<7.0.0',
 'rich>=13.4.2,<14.0.0',
 'types-pyyaml>=6.0.12.11,<7.0.0.0']

entry_points = \
{'console_scripts': ['clientele = src.cli:cli_group']}

setup_kwargs = {
    'name': 'clientele',
    'version': '0.3.1',
    'description': 'Typed API Clients from OpenAPI schemas',
    'long_description': "# ⚜️ Clientele\n\n# Typed API Clients from OpenAPI schemas\n\n![clientele_logo](https://github.com/beckett-software/clientele/blob/main/docs/clientele.jpeg?raw=true)\n\nClientele lets you generate fully-typed, functional, API Clients from OpenAPI schemas.\n\nIt uses modern tools to be blazing fast and type safe.\n\nPlus - there is no complex boilerplate and the generated code is very small.\n\n## Features\n\n* Fully typed API Client using Pydantic.\n* Minimalist and easy to use - the generated code is designed for readability.\n* Choose either sync or async - we support both, and you can switch between them easily.\n* Supports authentication (curently only HTTP Bearer and HTTP Basic auth).\n* Written entirely in Python - no need to install other languages to use OpenAPI.\n* The client footprint is minimal - it only requires `httpx` and `pydantic`.\n* Supports your own configuration - we provide an entry point that will never be overwritten.\n\nWe're built on:\n\n* [Pydantic 2.0](https://docs.pydantic.dev/latest/)\n* [httpx](https://www.python-httpx.org/)\n* [openapi-core](https://openapi-core.readthedocs.io/en/latest/)\n\n## Install\n\n```sh\npoetry add clientele\n```\n\n## Usage\n\n```sh\nclientele generate -f path/to/file.json -o my_client/ --asyncio t\n```\n\n[Read the docs](https://beckett-software.github.io/clientele/)\n",
    'author': 'Paul Hallett',
    'author_email': 'paulandrewhallett@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://beckett-software.github.io/clientele/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
