Advanced Usage
==============

(Scoped) Slots
--------------

Slots are used to add content at a certain location in a widget. You can find out what slots a widget supports by using
the Vuetify documentation. If you want to know what slots :code:`Select` has, search for :code:`v-select` on the
`Vuetify API explorer <https://vuetifyjs.com/en/api/>`_ or for this example use the `direct link
<https://vuetifyjs.com/en/api/v-select/>`_. In the component API you will find the slots it supports.

An example for using the slot 'no-data', which changes what the Select widget shows when it has no items:

Vuetify:

.. code-block:: html

    <v-select>
      <template v-slot:no-data>
        <v-list-item>
          <v-list-item-title>
            My custom no data message
          </v-list-item-title>
        </v-list-item>
      </template>
    </v-select>

ipyvuetify:

.. jupyter-execute::
    :hide-output:
    :hide-code:

    import ipyvuetify as v

.. jupyter-execute::

    v.Select(v_slots=[{
        'name': 'no-data',
        'children': [
            v.ListItem(children=[
                v.ListItemTitle(children=['My custom no data message'])])]
    }])

Scoped slots are used if the parent widget needs to share its scope with the content. In the example below the activator
props of the parent widget are used in the slot content.

Vuetify:

.. code-block:: html

    <v-tooltip>
        <template v-slot:activator="tooltip">
            <v-btn v-bind="tooltip.props" color="primary">
                button with tooltip
            </v-btn>
        </template>
        Insert tooltip text here
    </v-tooltip>

ipyvuetify:

.. jupyter-execute::

    v.Container(children=[
        v.Tooltip(location='bottom', v_slots=[{
            'name': 'activator',
            'variable': 'tooltip',
            'children': v.Btn(v_on='tooltip.props', color='primary', children=[
                'button with tooltip'
            ]),
        }], children=['Insert tooltip text here'])
    ])

In the Vuetify examples you will actually see:

.. code-block:: html

    ...
    <template v-slot:activator="{ props }">
        <v-btn v-bind="props">
    ...

Instead of the functionally equivalent (like used in the example above):

.. code-block:: html

    ...
    <template v-slot:activator="tooltip">
        <v-btn v-bind="tooltip.props">
    ...

The :code:`{ props }` is JavaScript syntax for destructuring an object. It takes the 'props' attribute from an object and
exposes it as the 'props' variable.

.. note::

    The 'default' slot can be ignored, this is where the content defined in the :code:`children` attribute goes.

Responsive Layout
-----------------

When making dashboards with Voilà you can change the layout depending on the user's screen size. This is done with a `grid
system <https://vuetifyjs.com/en/components/grids/>`_. For example on a laptop (breakpoint md) you could fit two
elements next to each other while on a smartphone (defined with 'cols' as default) you would want one element to take up
the full width:

.. jupyter-execute::
    :hide-output:

    v.Row(children=[
        v.Col(cols=12, md=6, children=[
            v.Card(variant='outlined', style_='height: 400px', children=[f'Element {i}'])
        ]) for i in range (1,3)
    ])

Which displays on a laptop as:

.. image:: images/responsive-laptop.png
    :width: 680

On a phone as:

.. image:: images/responsive-mobile.png
    :width: 263

In the `display section <https://vuetifyjs.com/en/styles/display/>`_ you will find CSS helper classes to do more
customizations based on screen size.

Event modifiers
---------------

In Vue `event modifiers <https://vuejs.org/guide/essentials/event-handling.html#event-modifiers>`_ can be used to change event behavior.

For example when you have two nested elements and want a different click handler for the inner and outer element, the
``stop`` event modifier can be used by appending ``.stop`` to the event name:

.. jupyter-execute::

    icon = v.Icon(end=True, children=['mdi-account-lock'])
    btn = v.Btn(color='primary', children=[
        'button',
        icon
    ])

    icon.on_event('click.stop', lambda *args: print('icon clicked'))
    btn.on_event('click', lambda *args: print('btn clicked'))

    v.Container(children=[
        btn
    ])

    # Note: the event handlers won't work in this page because there is no active kernel.

v-model arguments
-----------------

When you see a ``v-model`` argument such as ``v-model:rail`` in Vuetify syntax, it means the attribute has a `two-way binding
<https://vuejs.org/guide/components/v-model.html#v-model-arguments>`_ (like the default ``v-model``). Vue
automatically listens to an event named ``update:<attributeNameInCamelCase>``.

We can achieve the same manually in ipyvuetify by setting an event handler
``<widget>.on_event('update:<attributeNameInCamelCase>', <function>)``

Vuetify:

..  code-block:: none

    <v-navigation-drawer v-model:rail="someProperty" ...

ipyvuetify:

.. code-block:: none

    drawer = v.NavigationDrawer(rail=True, ...)

    def update_rail(widget, event, data):
        drawer.rail = data

    drawer.on_event('update:rail', update_rail)
