# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src', 'src.generators', 'src.template']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'httpx>=0.24.1,<0.25.0',
 'ipython>=8.14.0,<9.0.0',
 'openapi-core==0.18.0',
 'pydantic>=2.0.3,<3.0.0',
 'pyyaml>=6.0.1,<7.0.0',
 'rich>=13.4.2,<14.0.0',
 'structlog>=23.1.0,<24.0.0',
 'types-pyyaml>=6.0.12.11,<7.0.0.0']

entry_points = \
{'console_scripts': ['clientele = src.cli:cli_group']}

setup_kwargs = {
    'name': 'clientele',
    'version': '0.2.0',
    'description': 'Typed API Clients from OpenAPI specs',
    'long_description': "#  ⚜️ Clientele\n\n### Typed API Clients from OpenAPI specs\n\n![clientele_logo](https://github.com/beckett-software/clientele/blob/main/docs/clientele.jpeg?raw=true)\n\nClientele lets you generate fully-typed, functional, API Clients from OpenAPI specs.\n\nIt uses modern tools to be blazing fast and type safe. \n\nPlus - there is no complex boilerplate and the generated code is very small.\n\n## Features\n\n* Fully typed API Client using Pydantic.\n* Minimalist and easy to use - the generated code is tiny.\n* Choose either sync (default) or async - we support both.\n* Generates authentication code for you (curently only supports HTTP Bearer auth)\n* Written entirely in Python - no need to install other languages to use OpenAPI.\n\nWe're built on:\n\n* [Pydantic 2.0](https://docs.pydantic.dev/latest/)\n* [httpx](https://www.python-httpx.org/)\n* [openapi-core](https://openapi-core.readthedocs.io/en/latest/)\n\n## Install\n\n```sh\npoetry add clientele\n```\n\n## Usage\n\n### From URLs\n\n```sh\nclientele generate -u http://URL_TO_OPEN_API.json -o output/\n```\n\n### From files\n\n```sh\nclientele generate -f path/to/file.json -o output/\n```\n\n### Async Client\n\n```sh\nclientele generate -f path/to/file.json -o output/ --asyncio t\n```\n\n## Authentication\n\nIf your OpenAPI spec provides security information for the following authentication methods:\n\n* HTTP Bearer\n\nThen clientele will provide you information on the environment variables you need to set to\nmake this work during the generation. For example:\n\n```sh\nPlease set\n* MY_CLIENT_AUTH_USER_KEY\n* MY_CLIENT_AUTH_PASS_KEY\nenvironment variable to use basic authentication\n```\n",
    'author': 'Paul Hallett',
    'author_email': 'paulandrewhallett@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/beckett-software/clientele',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
