# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyrandonaut']

package_data = \
{'': ['*']}

install_requires = \
['numpy==1.23.1', 'pandas==1.4.3', 'randonautentropy==1.0.2', 'scipy==1.9.0']

entry_points = \
{'console_scripts': ['pyrandonaut = pyrandonaut.__init__:__main__']}

setup_kwargs = {
    'name': 'pyrandonaut',
    'version': '0.1.8',
    'description': 'Open-source quantum random coordinate generation for randonauts <3',
    'long_description': None,
    'author': 'alicemandragora',
    'author_email': 'openrandonaut@riseup.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
