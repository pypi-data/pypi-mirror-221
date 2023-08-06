# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tidychef',
 'tidychef.acquire',
 'tidychef.acquire.csv',
 'tidychef.acquire.python',
 'tidychef.acquire.xls',
 'tidychef.acquire.xlsx',
 'tidychef.against',
 'tidychef.against.implementations',
 'tidychef.column',
 'tidychef.datafuncs',
 'tidychef.direction',
 'tidychef.exceptions',
 'tidychef.lookup',
 'tidychef.lookup.engines',
 'tidychef.models',
 'tidychef.models.source',
 'tidychef.notebook',
 'tidychef.notebook.preview',
 'tidychef.notebook.preview.html',
 'tidychef.output',
 'tidychef.selection',
 'tidychef.selection.csv',
 'tidychef.selection.filters',
 'tidychef.selection.xls',
 'tidychef.selection.xlsx',
 'tidychef.utils',
 'tidychef.utils.cellutils',
 'tidychef.utils.decorators',
 'tidychef.utils.fileutils',
 'tidychef.utils.http']

package_data = \
{'': ['*']}

install_requires = \
['cachecontrol>=0.13.1,<0.14.0',
 'filelock>=3.12.2,<4.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'openpyxl>=3.1.2,<4.0.0',
 'requests>=2.31.0,<3.0.0',
 'tabulate>=0.9.0,<0.10.0',
 'validators>=0.20.0,<0.21.0',
 'xlrd>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'tidychef',
    'version': '0.1.0',
    'description': 'Python package for transforming human readable tables into tidy data',
    'long_description': 'None',
    'author': 'mikeAdamss',
    'author_email': 'mikelovesbooks@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
