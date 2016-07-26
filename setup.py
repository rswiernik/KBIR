try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'kbir',
    'description': 'Keyboard Intermediate Representation',
    'author': 'Reed Swiernik',
    'author_email': 'rswiernik@csh.rit.edu',
    'url': 'https://github.com/rswiernik/KBIR',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['kbir'],
    'scripts': [],
}

setup(**config)
