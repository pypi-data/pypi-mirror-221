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
    'version': '0.1.1',
    'description': 'Python framework for transforming tabulated data with visual relationships into tidy data',
    'long_description': '# Tidychef\n\n![Tests](https://github.com/mikeAdamss/tidychef/actions/workflows/tests.yml/badge.svg)\n![The test coverage for tidychef is 100%](./jupyterbook/images/coverage-100.svg)\n![Static Badge](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20-blue)\n\nTidychef is a python framework to enable “data extraction for humans” via simple python beginner friendly "recipes". It aims at allowing users to easily transform tabulated data sources that use visual relationships (human readable only data) into simple machine readable "tidy data" in a repeatable way.\n\ni.e: it allows you to reliably turn something that looks like this: \n\n![](./jupyterbook/images/bands-before.png)\n\ninto something that looks like this:\n\n![](./jupyterbook/images/bands-after.png)\n_Note: image cropped for reasons of practicality._\n\nTidychef is **designed to allow even novice python users or analysts to quickly become productive** but also has an advanced feature set and is designed to be readily and easily extended (adding new source of tabulated data, your own use case specific methods and filters and domain specific validation etc are all possible and documented in detail).\n\nIn depth training material, examples and technical documentation [can be found here](https://mikeadamss.github.io/tidychef/intro.html#).\n\n## Installation\n\n```\npip install tidychef\n```\n\n## Acknowlagements\n\nTidychef is directly inspired by the python package [databaker](https://github.com/sensiblecodeio/databaker) created by [The Sensible Code Company](https://sensiblecode.io/) in partnership with the United Kingdoms [Office For National Statistics](https://www.ons.gov.uk/).\n\nWhile I liked [databaker](https://github.com/sensiblecodeio/databaker) and successfully worked with it on multiple ETL projects over the course of almost a decade, this software should be considered the culmination of that work and the lessons learned from that time.',
    'author': 'mikeAdamss',
    'author_email': 'mikelovesbooks@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mikeAdamss/tidychef',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
