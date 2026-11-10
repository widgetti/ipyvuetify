"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
import inspect
import re
from datetime import datetime
from pathlib import Path
from shutil import copytree

from docutils import nodes
from markdown_it import MarkdownIt
from sphinx.ext.autodoc import AttributeDocumenter, ClassDocumenter
from sphinx.util.docutils import SphinxDirective
from traitlets import TraitType

# -- Project information -----------------------------------------------------

project = "ipyvuetify"
copyright = f"2019-{datetime.now().year}, Mario Buikhuizen"
author = "Mario Buikhuizen"
release = "3.1.1"

# -- General configuration ---------------------------------------------------

extensions = [
    "jupyter_sphinx",
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- API reference -----------------------------------------------------------

# the widget classes are defined in submodules but documented in the namespace they are used from,
# e.g. ipyvuetify.Btn instead of ipyvuetify.generated.Btn
autosummary_imported_members = True
# keeps the signatures of the reacton components readable, they have a type for every parameter
autodoc_typehints = "none"

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


# The help of the generated traits contains the Markdown descriptions of the Vuetify API, which reads
# well in help() and editors. In the docs it is rendered to HTML with the markdown directive.
markdown = MarkdownIt("commonmark", {"html": False})


def markdown_to_nodes(text):
    tokens = markdown.parse(text)
    # a single paragraph is rendered inline, so it can follow the name of a :param: on the same line
    if [token.type for token in tokens] == ["paragraph_open", "inline", "paragraph_close"]:
        return [nodes.paragraph("", "", nodes.raw("", markdown.renderInline(text), format="html"))]
    return [nodes.raw("", markdown.render(text), format="html")]


class MarkdownDirective(SphinxDirective):
    """Renders its content as Markdown, the content is not parsed as reST so it needs no escaping."""

    has_content = True

    def run(self):
        return markdown_to_nodes("\n".join(self.content))


def markdown_directive(text, indent=""):
    return [f"{indent}.. markdown::", "", *(f"{indent}    {line}" for line in text.splitlines())]


class WidgetClassDocumenter(ClassDocumenter):
    """Documents the inherited members of a class, except those of ipywidgets and traitlets.

    :inherited-members: can't do this, as the ipyvue Events mixin comes after ipywidgets.Widget in
    the MRO of the widgets.
    """

    def get_object_members(self, want_all):
        check, members = super().get_object_members(want_all)
        return check, [member for member in members if not self.from_base_library(member.__name__)]

    def from_base_library(self, name):
        defined_in = next((cls for cls in self.object.__mro__ if name in vars(cls)), None)
        module = getattr(defined_in, "__module__", None) or ""
        return module.split(".")[0] in ("ipywidgets", "traitlets")


class TraitDocumenter(AttributeDocumenter):
    """Describe traits by the values they accept instead of the docstring of the trait class."""

    objtype = "trait"
    directivetype = AttributeDocumenter.objtype
    priority = AttributeDocumenter.priority + 1

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, TraitType)

    def should_suppress_value_header(self):
        return True

    def get_doc(self):
        # the generated Union traits can contain the same type multiple times
        info = " or ".join(dict.fromkeys(self.object.info().split(" or ")))
        text = f"{info[0].upper()}{info[1:]}."
        if self.object.help:
            text += "\n\n" + self.object.help
        return [markdown_directive(text)]


def convert_component_params(app, what, name, obj, options, lines):
    """Render the Markdown of the :param ...: fields that reacton generates from the trait help."""
    if what != "function" or not name.startswith("ipyvuetify.components."):
        return
    converted = []
    field, description = None, []

    def add_field():
        if field is not None:
            converted.append(field)
            converted.extend(markdown_directive("\n".join(description).strip(), indent="    "))

    for line in lines:
        param = re.match(r"\s*(:param \w+:)(.*)", line)
        if param:
            add_field()
            # reacton puts the fields directly below the docstring of the widget class
            if converted and converted[-1].strip() and not converted[-1].startswith(" "):
                converted.append("")
            field, description = param[1], [param[2]]
        elif field is not None:
            description.append(line)
        else:
            converted.append(line)
    add_field()
    lines[:] = converted


# imported from other packages, but meant to be used from ipyvuetify
REEXPORTS = {"use_event"}


def skip_foreign_imports(app, what, name, obj, skip, options):
    """Skip classes and functions that a module imports from other packages (e.g. reacton)."""
    if (inspect.isclass(obj) or inspect.isfunction(obj)) and name not in REEXPORTS:
        module = getattr(obj, "__module__", None) or ""
        top_level = "." not in getattr(obj, "__qualname__", name)
        if top_level and not module.startswith("ipyvuetify"):
            return True
    return None


def setup(app):
    app.add_directive("markdown", MarkdownDirective)
    app.add_autodocumenter(WidgetClassDocumenter, override=True)
    app.add_autodocumenter(TraitDocumenter)
    app.connect("autodoc-skip-member", skip_foreign_imports)
    app.connect("autodoc-process-docstring", convert_component_params)

    def copy_jupyter_vuetify_bundle(app, exception):
        if exception is not None or app.builder.format != "html":
            return

        root = Path(__file__).parent.parent
        dist = root / "js" / "dist"
        static_bundle = Path(app.outdir) / "_static" / "jupyter-vuetify"
        if dist.exists():
            copytree(dist, static_bundle, dirs_exist_ok=True)

    app.connect("build-finished", copy_jupyter_vuetify_bundle)
