# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chainfury_server',
 'chainfury_server.api',
 'chainfury_server.commons',
 'chainfury_server.database_utils',
 'chainfury_server.engines',
 'chainfury_server.plugins',
 'chainfury_server.plugins.echo',
 'chainfury_server.schemas']

package_data = \
{'': ['*'],
 'chainfury_server': ['examples/*',
                      'static/*',
                      'static/assets/*',
                      'static/script/*']}

install_requires = \
['PyJWT[crypto]==2.6.0',
 'SQLAlchemy==1.4.47',
 'black==23.3.0',
 'chainfury',
 'fastapi==0.95.2',
 'fire==0.5.0',
 'passlib==1.7.4',
 'requests==2.28.2',
 'uvicorn==0.20.0']

extras_require = \
{':extra == "langflow"': ['PyMySQL==1.0.3'],
 'langflow': ['chromadb==0.3.21',
              'dill==0.3.6',
              'docstring-parser==0.15',
              'fake-useragent==1.1.3',
              'google-api-python-client==2.86.0',
              'google-search-results==2.4.2',
              'huggingface-hub==0.13.4',
              'langchain>=0.0.186',
              'lxml==4.9.2',
              'networkx==3.1',
              'openai>=0.27.7',
              'pandas==1.5.3',
              'psycopg2-binary==2.9.6',
              'pyarrow==11.0.0',
              'pypdf==3.8.1',
              'pysrt==1.1.2',
              'rich==13.3.4',
              'typer==0.7.0',
              'types-pyyaml==6.0.12.9',
              'unstructured>=0.5.11']}

entry_points = \
{'console_scripts': ['cf_server = chainfury_server.server:main',
                     'chainfury_server = chainfury_server.server:main']}

setup_kwargs = {
    'name': 'chainfury-server',
    'version': '1.1.0',
    'description': 'ChainFury Server is the open source server for running ChainFury Engine!',
    'long_description': '# ChainFury Server\n\nThis is a package separate from `chainfury` which provides the python execution engine.\n',
    'author': 'NimbleBox Engineering',
    'author_email': 'engineering@nimblebox.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NimbleBoxAI/ChainFury',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
