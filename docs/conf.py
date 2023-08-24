"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Project information -----------------------------------------------------

project = "ipyvuetify"
copyright = "2020, Mario Buikhuizen"
author = "Mario Buikhuizen"
release = "1.2.2"

# -- General configuration ---------------------------------------------------

extensions = ["jupyter_sphinx", "sphinx_rtd_theme"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
