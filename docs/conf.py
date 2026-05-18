"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
from datetime import datetime
from pathlib import Path
from shutil import copytree

# -- Project information -----------------------------------------------------

project = "ipyvuetify"
copyright = f"2019-{datetime.now().year}, Mario Buikhuizen"
author = "Mario Buikhuizen"
release = "3.0.0.dev0"

# -- General configuration ---------------------------------------------------

extensions = ["jupyter_sphinx", "sphinx_design"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
jupyter_sphinx_embed_url = "jupyter-vuetify-embed-amd.js"
html_sidebars = {
    "**": [],
}

# -- Theme configuration -----------------------------------------------------

html_theme_options = {
    "use_edit_page_button": True,
    "show_prev_next": True,
    "navbar_start": ["navbar-logo"],
    "secondary_sidebar_items": [
        "page-toc.html",
        "searchbox.html",
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


def setup(app):
    def copy_jupyter_vuetify_bundle(app, exception):
        if exception is not None or app.builder.format != "html":
            return

        root = Path(__file__).parent.parent
        dist = root / "js" / "dist"
        static_bundle = Path(app.outdir) / "_static" / "jupyter-vuetify"
        if dist.exists():
            copytree(dist, static_bundle, dirs_exist_ok=True)

    app.connect("build-finished", copy_jupyter_vuetify_bundle)
