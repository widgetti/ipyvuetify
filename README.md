ipyvuetify
===============================

[![Documentation](http://readthedocs.org/projects/ipyvuetify/badge/?version=latest)](https://ipyvuetify.readthedocs.io/en/latest/?badge=latest)
[![Version](https://img.shields.io/npm/v/jupyter-vuetify.svg)](https://www.npmjs.com/package/jupyter-vuetify)
[![Version](https://img.shields.io/pypi/v/ipyvuetify.svg)](https://pypi.python.org/project/ipyvuetify)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/ipyvuetify.svg)](https://anaconda.org/conda-forge/ipyvuetify)

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mariobuikhuizen/ipyvuetify/master?filepath=examples%2FExamples.ipynb)

Jupyter widgets based on [vuetify UI components](https://vuetifyjs.com/) which implement Google's
[Material Design Spec](https://material.io/) with the [Vue.js framework](https://vuejs.org/).

A small selection of widgets:

![ipyvuetify](https://user-images.githubusercontent.com/46192475/79730684-78954880-82f1-11ea-855b-43a2b619ca04.gif)

Installation
------------

To install use pip:

    $ pip install ipyvuetify
    $ jupyter nbextension enable --py --sys-prefix ipyvuetify
    
    # for Jupyter Lab < 3
    $ jupyter labextension install jupyter-vuetify


For a development installation (requires npm),

    $ git clone https://github.com/mariobuikhuizen/ipyvuetify.git
    $ cd ipyvuetify
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix ipyvuetify
    $ jupyter nbextension enable --py --sys-prefix ipyvuetify

Documentation
-------------

To get started with using ipyvuetify, check out the full documentation

https://ipyvuetify.readthedocs.io/

Usage
-----

For examples see the [example notebook](examples/Examples.ipynb).

The [Vuetify documentation](https://vuetifyjs.com/components/buttons#buttons) can be used to find all available
components and attributes (in the left side bar or use the search field). Ipyvuetify tries to stay close to the Vue.js 
and Vuetify template syntax, but there are some differences:

| Description | Vuetify | ipyvuetify |
|-------------|---------|------------|
| Component names are in CamelCase and the v- prefix is stripped | `<v-list-tile .../>` | `ListTile(...)` |
| Child components and text are defined in the children traitlet| `<v-btn>text <v-icon .../></v-btn>` | `Btn(children=['text', Icon(...)])` |
| Flag attributes require a boolean value | `<v-btn round ...` | `Btn(round=True ...` |
| Attributes are snake_case | `<v-menu offset-y ..` | `Menu(offset_y=True ...` |
| The v_model attribute (value in ipywidgets) contains the value directly | `<v-slider v-model="some_property" ...` | `Slider(v_model=25...` |
| Event listeners are defined with on_event | `<v-btn @click='someMethod()' ...` | `button.on_event('click', some_method)` |
| | | `def some_method(widget, event, data):` |
| Regular HTML tags can made with the Html class | `<div>...</div>` | `Html(tag='div', children=[...])` |
| The attributes class and style need to be suffixed with an underscore | `<v-btn class="mr-3" style="..." >` | `Btn(class_='mr-3', style_='...')` |

### Advanced usage
#### .sync
The .sync property modifier functionality can be achieved by using an event named:  
`update:[propertyNameInCamelCase]`.
##### Vuetify:
```HTML
<v-navigation-drawer :mini-variant.sync=...
```
##### ipyvuetify:
```python
drawer = v.NavigationDrawer(mini_variant=True, ...)

def update_mini(widget, event, data):
    drawer.mini_variant = data`

drawer.on_event('update:miniVariant', update_mini)
```

### (scoped) slots
##### Vuetify:
```HTML
<v-menu>
  <template slot:activator="{ on }">
    <v-btn v-on="on">...</v-btn>
  </template>
  <v-list>
    ...
  </v-list>
</v-menu>
```
##### ipyvuetify:
```python
Menu(v_slots=[{
    'name': 'activator',
    'variable': 'x',
    'children': Btn(v_on='x.on', children=[...])
}], children=[
    List(...)
])
```
For non scoped slots `'scope': 'x'` and `v_on` can be omitted.

### Icons

Available icons:
 * https://material.io/resources/icons/ (deprecated)
 * https://pictogrammers.github.io/@mdi/font/4.5.95/ (since v1.2.0)

Alternate usage
---------------

For a more web development centric way of development and a closer match to the Vue/Vuetify api, VuetifyTemplate can be used. See the [example](examples/Examples%20template.ipynb) or [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/mariobuikhuizen/ipyvuetify/master?filepath=examples%2FExamples%20template.ipynb).

Make a sub class of VuetifyTemplate, define your own traitlets and set a template string. The traitlets will be accessible from the template as if they were in a vue-model. Methods can be called by defining a method with a prefix `vue_` e.g. `def vue_button_click(self, data)` and calling it from the template e.g. `@click="button_click(e)"`.
