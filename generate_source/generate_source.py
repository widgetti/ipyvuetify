import os
import shutil
import subprocess
from .generate_schema import generate_schema

here = os.path.dirname(os.path.abspath(__file__))

vuetify_api = f'{here}/vuetify_api_1.5.12.json'
base_schema = f'{here}/base.json'
build_dir = f'{here}/build'
widget_gen_schema = f'{build_dir}/widget_gen_schema.json'

widgetgen = f'{here}/node_modules/.bin/widgetgen'

es6_template = f'{here}/es6-template.njk'
python_template = f'{here}/python.njk'

project_dir = f'{here}/..'
destination_js = f'{project_dir}/js/lib/generated'
destination_python = f'{project_dir}/ipyvuetify/generated'


def reset_dir(name):
    if os.path.isdir(name):
        shutil.rmtree(name)

    os.mkdir(name)


def generate():
    if not os.path.isdir(build_dir):
        os.mkdir(build_dir)

    generate_schema(vuetify_api, base_schema, widget_gen_schema)

    subprocess.check_call('npm install', cwd=here, shell=True)

    reset_dir(destination_js)
    subprocess.check_call(
        f'{widgetgen} -p json -o {destination_js} -t {es6_template} {widget_gen_schema} es6',
        shell=True)
    with open(f'{destination_js}/.eslintrc.js', 'w') as f:
        f.write('''
            module.exports = {
                rules: {
                    camelcase: 'off',
                    quotes: 'off'
                },
            };
        ''')

    reset_dir(destination_python)
    subprocess.check_call(
        f'{widgetgen} -p json -o {destination_python} -t {python_template} '
        f'{widget_gen_schema} python',
        shell=True)
