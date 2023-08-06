# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lib310_lite', 'lib310_lite.bigquery', 'lib310_lite.laser']

package_data = \
{'': ['*']}

install_requires = \
['bounded_pool_executor>=0.0.0',
 'dask-sql>=2022.11.0',
 'dask>=2022.11.0',
 'db-dtypes>=1.0.0',
 'distributed>=2022.11.0',
 'gcsfs>=2022.11.0',
 'google-cloud-bigquery>=3.2.0',
 'google-cloud>=0.34.0',
 'mysqlclient>=2.0.0',
 'numpy<1.23.0']

setup_kwargs = {
    'name': 'lib310-lite',
    'version': '0.1.0.dev13',
    'description': 'lib310 Lite Python Package',
    'long_description': 'None',
    'author': '310',
    'author_email': 'info@310.ai',
    'maintainer': 'Saman Fekri',
    'maintainer_email': 'saman@310.ai',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
