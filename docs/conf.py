# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# Add the project root to the system path so that Sphinx can find the package
sys.path.insert(0, os.path.abspath(".."))

from puffkit import __version__ as puffkit_version

project = "puffkit"
copyright = "2025, puffkit contributors"
author = "puffkit contributors"
release = puffkit_version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autosummary_generate = True

autodoc_typehints = "both"
autodoc_typehints_format = "short"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "private-members": True,
    "inherited-members": True,
    "show-inheritance": True,
    "member-order": "groupwise",
}

napoleon_include_init_with_doc = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "alabaster"
# html_theme = "sphinx_rtd_theme"
html_theme = "furo"
html_static_path = ["_static"]
