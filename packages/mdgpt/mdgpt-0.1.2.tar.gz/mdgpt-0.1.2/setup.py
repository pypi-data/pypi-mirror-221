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
    'version': '0.1.2',
    'description': 'Translate markdown files using OpenAI ChatGPT, and generate localized copies of each file.',
    'long_description': '# mdGPT - Mark Down General Purpose Transformer\n\nTranslate markdown files using OpenAI ChatGPT, and generate localized copies of each file.\n\n## Installation\n\n### Using pip\n\n```bash\npip install mdgpt\n```\n\nSet environment variable `OPENAI_API_KEY` or create it in a `.env` file\n\n```bash\nexport OPENAI_API_KEY=YOUR_API_KEY\n```\n\nDownload example prompts:\n\n```bash\ncurl -o prompts.yaml https://raw.githubusercontent.com/Djarnis/mdGPT/main/prompts.yaml\n```\n\nUse the example `WEBSITE_BUILDER` option from the prompts to build some example files;\n\n```bash\nmdbuild -d example -p prompts -l en\n```\n\nTo translate the markdown files into Finish (fi) versions, run this command:\n\n```bash\nmdtranslate -p prompts -d example -sl en -tl fi\n```\n\nAdjust the [prompts](prompts.yaml) to suit your needs.\n\n#### MODEL\n\nYou can change the `MODEL` to any engine supported by OpenAI, change the default temperature, and adjust max tokens.\n\n#### WEBSITE_BUILDER\n\n...\n\n#### URL_PROMPT\n\n...\n\n#### MARKDOWN_PROMPT\n\n...\n\n#### ONLY_INDEXES\n\nOptional boolean value, if you only want `index.md` files translated.\n\n#### FIELD_KEYS\n\nOptional list of frontmatter keys you want to tranlate.\n\n...\n\n---\n\n### Using repo source and Poetry:\n\n#### Step 1: Install Poetry\n\nPoetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.\n\nOn Unix-based systems like Linux and MacOS, you can install Poetry by using the following command in your terminal:\n\n```bash\ncurl -sSL https://install.python-poetry.org | python -\n```\n\nOn Windows, you can use PowerShell to install Poetry with the following command:\n\n```powershell\n(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -\n```\n\nYou can check if Poetry was installed correctly by running:\n\n```bash\npoetry --version\n```\n\n#### Step 2: Rename .env.tpl to .env\n\nIn your project directory, you have a file named .env.tpl which serves as a template for environment variables. To use this file, you should rename it to .env.\n\nOn Unix-based systems, use the following command:\n\n```bash\nmv .env.tpl .env\n```\n\nOn Windows, use the following command:\n\n```powershell\nrename .env.tpl .env\n```\n\n#### Step 3: Add OPENAI_API_KEY value to .env\n\nOpen your .env file in a text editor. You should see a line that looks something like this:\n\n```bash\nOPENAI_API_KEY=\n```\n\nAfter the equal sign, add your OpenAI API key in quotes. It should look something like this:\n\n```bash\nOPENAI_API_KEY="your-api-key-goes-here"\n```\n\nSave the .env file and close it.\n\n_Please note:_\n\n-   Make sure to replace "your-api-key-goes-here" with your actual OpenAI API key.\n-   Do not share your .env file or post it online, as it contains sensitive information.\n\n#### Step 4: Install mdGPT\n\nFrom the project directory, install mdGPT and its dependencies:\n\n```bash\npoetry install\n```\n\nThis installs mdGPT and all its dependencies, and you can now follow the example below.\n\n## Example\n\n### Build Markdown files\n\nThe example website ([./example/en](example/en)) was created using the `WEBSITE_BUILDER` option included in the [prompts.yaml](prompts.yaml) file.\n\n```bash\npoetry run mdbuild -d example -p prompts -l en\n```\n\nWhich will create these files in the ./example/en directory:\n\n-   index.md\n-   about.md\n-   contact.md\n-   history.md\n\n## Translate website\n\nTo translate the markdown files into Finish (fi) versions, run this command:\n\n```bash\npoetry run mdtranslate -p prompts -d example -sl en -tl fi\n```\n\nAnd you should get a `/fi` subdirectory ./example/fi/ containing these files, translated from their original English (en) source:\n\n-   index.md\n-   tietoja.md\n-   yhteystiedot.md\n-   historia.md\n',
    'author': 'Jeppe Bårris',
    'author_email': 'jeppe@barris.dk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Djarnis/mdGPT',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
