from setuptools import setup
import sys, os, imp

import sys, os, imp
from setuptools import Extension

dirname = os.path.dirname(__file__)
path_version = os.path.join(dirname, 'vaex/jupyter/_version.py')
version = imp.load_source('version', path_version)


name        = 'vaex'
author      = 'Maarten A. Breddels'
author_email= 'maartenbreddels@gmail.com'
license     = 'MIT'
version     = version.__version__
url         = 'https://www.github.com/maartenbreddels/vaex'
install_requires_jupyter = ['vaex-core', 'vaex-viz', 'bqplot>=0.10.1', 'ipyvolume>=0.4', 'ipyleaflet', 'ipympl']

setup(name=name+'-jupyter',
    version=version,
    description='Jupyter notebook and Jupyter lab support for vaex',
    url=url,
    author=author,
    author_email=author_email,
    install_requires=install_requires_jupyter,
    license=license,
    packages=['vaex.jupyter'],
    zip_safe=False,
    )
