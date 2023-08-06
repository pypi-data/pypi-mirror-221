# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['qsipy']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.25.0,<2.0.0']

setup_kwargs = {
    'name': 'qsipy',
    'version': '0.1.0',
    'description': 'Quantum State Interferometry with PYthon.',
    'long_description': '',
    'author': 'Quentin Marolleau',
    'author_email': 'quentin.marolleau@institutoptique.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
