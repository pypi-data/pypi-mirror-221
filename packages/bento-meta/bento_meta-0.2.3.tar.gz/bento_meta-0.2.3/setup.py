# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bento_meta',
 'bento_meta.mdb',
 'bento_meta.mdb.mdb_tools',
 'bento_meta.util',
 'bento_meta.util.cypher']

package_data = \
{'': ['*'], 'bento_meta': ['logs/*']}

install_requires = \
['PyYAML>=6.0.1',
 'bento-mdf>=0.9.1,<0.10.0',
 'delfick-project>=0.7.9,<0.8.0',
 'nanoid>=2.0.0,<3.0.0',
 'neo4j>=4.0',
 'requests>=2.28.1,<3.0.0',
 'setuptools>=65.4.1,<66.0.0',
 'tqdm>=4.64.1,<5.0.0']

extras_require = \
{':extra == "tools"': ['liquichange>=0.2.1,<0.3.0'],
 'tools': ['numpy>=1.23.5,<2.0.0',
           'pandas>=1.5.2,<2.0.0',
           'spacy>=3.4.3,<4.0.0',
           'click>=8.1.3,<9.0.0']}

scripts = \
['scripts/compare_models.py',
 'scripts/compare_val_set_terms.py',
 'scripts/make_model_changelog.py',
 'scripts/make_diff_changelog.py',
 'scripts/make_mapping_changelog.py']

setup_kwargs = {
    'name': 'bento-meta',
    'version': '0.2.3',
    'description': 'Python drivers for Bento Metamodel Database',
    'long_description': '# bento_meta - Object Model for the Bento Metamodel Database\n\nRead the docs at\n[https://cbiit.github.io/bento-meta/](https://cbiit.github.io/bento-meta/).\n\n\n',
    'author': 'Mark A. Jensen',
    'author_email': 'mark.jensen@nih.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'scripts': scripts,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
