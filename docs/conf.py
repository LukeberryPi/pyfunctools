# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use abspath to make it absolute, like shown here.

import sys
from os.path import dirname, abspath

sys.path.insert(1, dirname(dirname(abspath(__file__))))

# sys.path.insert(0, abspath('../pyfunc'))


# -- Project information -----------------------------------------------------

try:
    from pyfunctools import get_version
except ModuleNotFoundError or ImportError:
    try:
        from ..pyfunctools import get_version
    except ModuleNotFoundError or ImportError:
        print('Deu erro')

project = 'Pyfunctools'
copyright = '2021, Natan Santos'
author = 'Natan Santos'
version = get_version()

# The full version, including alpha/beta/rc tags
release = get_version(True)


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_theme', 'requirements.txt']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
