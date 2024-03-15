"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
from datetime import datetime

# -- Project information -----------------------------------------------------

project = "ipyvuetify"
copyright = f"2019-{datetime.now().year}, Mario Buikhuizen"
author = "Mario Buikhuizen"
release = "1.9.2"

# -- General configuration ---------------------------------------------------

extensions = ["jupyter_sphinx", "sphinx_rtd_theme", "sphinx_design"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# -- Theme configuration -----------------------------------------------------

html_theme_options = {
    "use_edit_page_button": True,
    "show_prev_next": True,
    "navbar_start": ["navbar-logo"],
    "secondary_sidebar_items": [
        "page-toc.html",
        "searchbox.html",
        "edit-this-page.html",
        "sourcelink.html",
    ],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/widgetti/ipyvuetify",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Pypi",
            "url": "https://pypi.org/project/ipyvuetify/",
            "icon": "fa-brands fa-python",
        },
    ],
    "logo": {
        "text": "ipyvuetify",
    },
}
html_context = {
    "github_user": "widgetti",
    "github_repo": "ipyvuetify",
    "github_version": "master",
    "doc_path": "docs",
}
