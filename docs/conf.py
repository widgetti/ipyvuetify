"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Project information -----------------------------------------------------

project = "ipyvuetify"
copyright = "2020, Mario Buikhuizen"
author = "Mario Buikhuizen"
release = "1.8.10"

# -- General configuration ---------------------------------------------------

extensions = ["jupyter_sphinx", "sphinx_rtd_theme", "autoapi.extension"]
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
}
html_context = {
    "github_user": "widgetti",
    "github_repo": "ipyvuetify",
    "github_version": "master",
    "doc_path": "docs",
}

# -- Options for autosummary/autodoc output ------------------------------------
autodoc_typehints = "description"
autoapi_dirs = ["../ipyvuetify"]
autoapi_member_order = "groupwise"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]


def skip_submodules(app, what, name, obj, skip, options):
    """Ignore the modules and packages taht are private

    Only necessary for those that are not using a leading underscore
    """
    privates = [
        ("module", "ipyvuetify.Html"),
        ("module", "ipyvuetify.VuetifyTemplate"),
        ("package", "ipyvuetify.generated"),
    ]

    # return `skip` when nothing is catch to keep skipping the private members
    return any([what == t and name == m for t, m in privates]) or skip


def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_submodules)
