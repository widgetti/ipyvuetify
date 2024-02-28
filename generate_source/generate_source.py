import shutil
import subprocess
from pathlib import Path

from pynpm import NPMPackage

from .generate_schema import generate_schema

here = Path(__file__).parent

vuetify_api = here / "vuetify_api.json"
base_schema = here / "base.json"
build_dir = here / "build"
widget_gen_schema = build_dir / "widget_gen_schema.json"

widgetgen = here / "node_modules" / ".bin" / "widgetgen"

es6_template = here / "es6-template.njk"
python_template = here / "python.njk"

project_dir = here.parent
destination_js = project_dir / "js" / "src" / "generated"
destination_python = project_dir / "ipyvuetify" / "generated"


def reset_dir(name: Path):
    shutil.rmtree(name, ignore_errors=True)
    name.mkdir(exist_ok=True)


def generate():

    build_dir.mkdir(exist_ok=True)

    generate_schema(vuetify_api, base_schema, widget_gen_schema)

    NPMPackage(here / "package.json")._run_npm("ci")

    reset_dir(destination_js)

    subprocess.check_call(
        f"{widgetgen} -p json -o {destination_js} -t {es6_template} {widget_gen_schema} es6",
        shell=True,
    )
    with open(destination_js / ".eslintrc.js", "w") as f:
        f.write(
            """
            module.exports = {
                rules: {
                    camelcase: 'off',
                    quotes: 'off'
                },
            };
        """
        )

    reset_dir(destination_python)
    subprocess.check_call(
        f"{widgetgen} -p json -o {destination_python} -t {python_template} "
        f"{widget_gen_schema} python",
        shell=True,
    )
