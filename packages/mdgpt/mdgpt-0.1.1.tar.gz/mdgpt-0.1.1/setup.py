# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mdgpt']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.27.8,<0.28.0',
 'pycountry>=22.3.5,<23.0.0',
 'python-dotenv>=1.0.0,<2.0.0',
 'python-frontmatter>=1.0.0,<2.0.0',
 'requests>=2.31.0,<3.0.0',
 'rich>=13.4.2,<14.0.0']

entry_points = \
{'console_scripts': ['mdbuild = mdgpt:build',
                     'mdengines = mdgpt:engines',
                     'mdtranslate = mdgpt:translate']}

setup_kwargs = {
    'name': 'mdgpt',
    'version': '0.1.1',
    'description': 'Translate and generate static site from Markdown files using ChatGTP',
    'long_description': None,
    'author': 'Jeppe Bårris',
    'author_email': 'jeppe@barris.dk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
