import sys
from pathlib import Path

from setuptools import Command, setup
from setuptools.command.egg_info import egg_info

ROOT = Path(__file__).parent
sys.path.append(str(ROOT))


def update_package_data(distribution) -> None:
    """Update package_data to catch changes during setup"""
    distribution.data_files = get_data_files()
    distribution.get_command_obj("build_py").finalize_options()


def rel(f: Path) -> str:
    """give the relative path of f with respect to ROOT"""
    # make sure the relative links are ok even when build in the isolated directory
    return str(f.relative_to(ROOT))


def js_prerelease(command: Command) -> None:
    """Decorator for building minified js/css prior to another command"""

    class DecoratedCommand(command):
        """Decorated command to install jsdeps first."""

        def run(self):
            """Run the command"""
            if not (ROOT / "prefix/share/jupyter/nbextensions/jupyter-vuetify/index.js").exists():
                from pynpm import NPMPackage

                from generate_source import generate_source

                npm = NPMPackage(ROOT / "js" / "package.json")
                npm._run_npm("ci")
                generate_source.generate()
                npm.run_script("build")

            self.distribution.data_files = get_data_files()
            command.run(self)

    return DecoratedCommand


def get_data_files():
    """files that need to be installed in specific locations upon installation."""
    nbext = [rel(f) for f in ROOT.glob("prefix/share/jupyter/nbextensions/jupyter-vuetify/*")]
    package = [
        rel(f) for f in ROOT.glob("prefix/share/jupyter/labextensions/jupyter-vuetify/package.json")
    ]
    labext = [
        rel(f) for f in ROOT.glob("prefix/share/jupyter/labextensions/jupyter-vuetify/static/*")
    ]
    nbconfig = [rel(f) for f in ROOT.glob("prefix/etc/nbconfig/notebook.d/jupyter-vuetify.json")]

    return [
        ("share/jupyter/nbextensions/jupyter-vuetify", nbext),
        ("share/jupyter/labextensions/jupyter-vuetify", package),
        ("share/jupyter/labextensions/jupyter-vuetify/static", labext),
        ("etc/jupyter/nbconfig/notebook.d", nbconfig),
    ]


setup(cmdclass={"egg_info": js_prerelease(egg_info)})
