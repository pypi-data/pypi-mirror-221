# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apacai',
 'apacai.api_resources',
 'apacai.api_resources.abstract',
 'apacai.api_resources.experimental',
 'apacai.datalib',
 'apacai.tests',
 'apacai.tests.asyncio']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp', 'requests>=2.20', 'tqdm']

extras_require = \
{':python_version < "3.8"': ['typing-extensions']}

setup_kwargs = {
    'name': 'apacai',
    'version': '0.1.0',
    'description': 'Python client library for the APACAI API',
    'long_description': 'None',
    'author': 'APACAI',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/APACAI-API.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
