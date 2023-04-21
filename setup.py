from __future__ import print_function

import glob
from pathlib import Path

from pynpm import NPMPackage
from setuptools import Command, setup
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info
from setuptools.command.sdist import sdist

from generate_source import generate

ROOT = Path(__file__).parent


def update_package_data(distribution) -> None:
    """Update package_data to catch changes during setup"""
    build_py = distribution.get_command_obj("build_py")
    distribution.data_files = get_data_files()
    build_py.finalize_options()


def js_prerelease(command: Command, strict: bool = False) -> None:
    """Decorator for building minified js/css prior to another command"""

    class DecoratedCommand(command):
        """Decorated command to install jsdeps first."""

        def run(self):
            """Run the command"""
            self.distribution.run_command("generate_source")
            self.distribution.run_command("jsdeps")
            command.run(self)
            update_package_data(self.distribution)

    return DecoratedCommand


class NPM(Command):
    """Install package.json dependencies using npm."""

    def initialize_options(self):
        """Ignore initialize_options."""
        pass

    def finalize_options(self):
        """Ignore finalize_options."""
        pass

    def run(self):
        """Run the command."""
        NPMPackage(ROOT / "js" / "package.json").install()
        update_package_data(self.distribution)


class GenerateSource(Command):
    """Generate source from api specification"""

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):

        generate()


def get_data_files():
    return [
        (
            "share/jupyter/nbextensions/jupyter-vuetify",
            glob.glob("ipyvuetify/nbextension/*"),
        ),
        (
            "share/jupyter/labextensions/jupyter-vuetify",
            glob.glob("ipyvuetify/labextension/package.json"),
        ),
        (
            "share/jupyter/labextensions/jupyter-vuetify/static",
            glob.glob("ipyvuetify/labextension/static/*"),
        ),
        ("etc/jupyter/nbconfig/notebook.d", ["jupyter-vuetify.json"]),
    ]


setup(
    cmdclass={
        "build_py": js_prerelease(build_py),
        "egg_info": js_prerelease(egg_info),
        "sdist": js_prerelease(sdist, strict=True),
        "jsdeps": NPM,
        "generate_source": GenerateSource,
    },
)
