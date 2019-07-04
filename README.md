ipyvuetify
===============================

[![Version](https://img.shields.io/npm/v/jupyter-vuetify.svg)](https://www.npmjs.com/package/jupyter-vuetify)
[![Version](https://img.shields.io/pypi/v/ipyvuetify.svg)](https://pypi.python.org/mariobuikhuizen/ipyvuetify)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mariobuikhuizen/ipyvuetify/master?filepath=examples%2FExamples.ipynb)

Jupyter widgets based on [vuetify UI components](https://vuetifyjs.com) which implement Google's 
[Material Design Spec](https://material.io/) with the [Vue.js framework](https://vuejs.org/).

Installation
------------

To install use pip:

    $ pip install ipyvuetify
    $ jupyter nbextension enable --py --sys-prefix ipyvuetify


For a development installation (requires npm),

    $ git clone https://github.com/mariobuikhuizen/ipyvuetify.git
    $ cd ipyvuetify
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix ipyvuetify
    $ jupyter nbextension enable --py --sys-prefix ipyvuetify

Usage
-----

For examples see the [example notebook](examples/Examples.ipynb).

The [Vuetify documentation](https://vuetifyjs.com/en/components/buttons#button) can be used to find all available 
components and attributes (in the left side bar or use the search field). Ipyvuetify tries to stay close to the Vue.js 
and Vuetify template syntax, but there are some differences:

| Description | Vuetify | ipyvuetify |
|-------------|---------|------------|
| Component names are in CamelCase and the v- prefix is stripped | `<v-list-tile .../>` | `ListTile(...)` |
| Child components and text are defined in the children traitlet| `<v-btn>text <v-icon .../></v-btn>` | `Btn(children=['text', Icon(...)])` |
| Flag attributes require a boolean value | `<v-btn round ...` | `Btn(round=True ...` |
| Attributes are snake_case | `<v-menu offset-y ..` | `Menu(offset_y=True ...` |
| The v_model attribute (value in ipywidgets) contains the value directly | `<v-slider v-model="some_property" ...` | `Slider(v_model=25...` |
| Scoped slots are not yet implemented, use slot instead | `<v-menu><template slot:activator="{ on }"><v-btn v-on=on>` | `Menu(children=[Btn(slot='activator',...), ...]` 
| Event listeners are defined with on_event | `<v-btn @click='someMethod()' ...` | `button.on_event('click', some_method)` |
| | | `def some_method(widget, event, data):` |
| Regular HTML tags can made with the Html class | `<div>...</div>` | `Html(tag='div', children=[...])` |
| The attributes class and style need to be suffixed with an underscore | `<v-btn class="mr-3" style="..." >` | `Btn(class_='mr-3', style_='...')` |

