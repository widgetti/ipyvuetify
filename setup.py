import sys
from pathlib import Path

from pynpm import NPMPackage
from setuptools import Command, setup
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info
from setuptools.command.sdist import sdist

ROOT = Path(__file__).parent
sys.path.append(str(ROOT))

from generate_source import generate_source  # noqa


def update_package_data(distribution) -> None:
    """Update package_data to catch changes during setup"""
    distribution.data_files = get_data_files()
    distribution.get_command_obj("build_py").finalize_options()


def js_prerelease(command: Command) -> None:
    """Decorator for building minified js/css prior to another command"""

    class DecoratedCommand(command):
        """Decorated command to install jsdeps first."""

        def run(self):
            """Run the command"""
            NPMPackage(ROOT / "js" / "package.json").install()
            generate_source.generate()
            self.distribution.data_files = get_data_files()
            command.run(self)

    return DecoratedCommand


def get_data_files():
    """files that need to be installed in specific locations upon installation."""

    nbext = [str(f.relative_to(ROOT)) for f in ROOT.glob("ipyvuetify/nbextension/*")]
    labext_package = [
        str(f.relative_to(ROOT))
        for f in ROOT.glob("ipyvuetify/labextension/package.json")
    ]
    labext_static = [
        str(f.relative_to(ROOT)) for f in ROOT.glob("ipyvuetify/labextension/static/*")
    ]
    nbconfig = [str(f.relative_to(ROOT)) for f in ROOT.glob("jupyter-vuetify.json")]

    return [
        ("share/jupyter/nbextensions/jupyter-vuetify", nbext),
        ("share/jupyter/labextensions/jupyter-vuetify", labext_package),
        ("share/jupyter/labextensions/jupyter-vuetify/static", labext_static),
        ("etc/jupyter/nbconfig/notebook.d", nbconfig),
    ]


setup(
    cmdclass={
        "build_py": js_prerelease(build_py),
        "egg_info": js_prerelease(egg_info),
        "sdist": js_prerelease(sdist),
    },
)
