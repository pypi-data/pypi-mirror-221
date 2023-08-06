# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['biosen12']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'biosen12',
    'version': '2023.7.25',
    'description': '',
    'long_description': '# BioSEN12',
    'author': 'Juan Sensio',
    'author_email': 'it@earthpulse.es',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
