"""
All the process that can be run using nox.

The nox run are build in isolated environment that will be stored in .nox. to force the venv update, remove the .nox/xxx folder.
"""

import nox


@nox.session(reuse_venv=True)
def lint(session):
    """Apply the pre-commits."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "-a", *session.posargs)


@nox.session(reuse_venv=True)
def docs(session):
    """Build the documentation."""
    session.install("jupyter-packaging", "jupyterlab")
    session.install(".[doc]")
    session.run("sphinx-build", "-v", "-b", "html", "docs", "docs/_build/html")
