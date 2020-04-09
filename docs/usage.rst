Usage
=====

This page shows how to use ipyvuetify and explains how it is different from other widget libraries you may know such as
ipywidgets.

Create an ipyvuetify widget
---------------------------

Below you see how to create an ipyvuetify widget.

.. jupyter-execute::

    import ipyvuetify as v

    my_select = v.Select(
        label='Fruits',
        items=['Apple', 'Pear', 'Cherry'])
    my_select

Attributes can be changed at a later time by:

.. code-block:: python

    my_select.items = [*my_select.items, 'Banana']

.. note::
    A new List is created to change the items. In-place mutations of List and Dict, e.g. :code:`my_select.append(
    'Banana')`, are not detected by ipywidgets.

What widgets are available and how they look can be found in the
`Vuetify documentation <https://vuetifyjs.com/components/selects/>`_. Browse the side bar on the left hand side and
select a widget, then click <> on the right hand side on an example to see the source code for it. The HTML code may
seem unfamiliar at first, but this documentation will guide you through it. For starters to translate the Vuetify widget
names, which are starting with :code:`v-`, to ipyvuetify, remove the :code:`v-` prefix and capitalize the remaining
name. E.g :code:`v-select` becomes Select.

Equivalent Vuetify syntax of the example above:

.. code-block:: html

    <v-select label="Fruits" :items="['Apple', 'Pear', 'Cherry']" />

Setting Attributes
------------------

When translating from Vuetify HTML to Python, some attributes have to be treated different.

Python uses snake_case to separate words in attributes, while Vuetify uses kebab-case. For example the attribute
:code:`append-icon` becomes :code:`append_icon`:

Vuetify:

.. code-block:: html

    <v-select append-icon="mdi-gamepad-down" label="Fruits" />

ipyvuetify:

.. jupyter-execute::

    v.Select(append_icon='mdi-gamepad-down', label='Fruits')


In HTML attributes don't have to have values, just defining the attribute is enough to use it as a boolean. In Python we
have to set the value to True. For example :code:`clearable` becomes :code:`clearable=True`:

Vuetify:

.. code-block:: html

    <v-select clearable label="Fruits" :items="['Apple', 'Pear', 'Cherry']" value="Apple" />

ipyvuetify:

.. jupyter-execute::

    v.Select(clearable=True, label='Fruits', items=['Apple', 'Pear', 'Cherry'], value='Apple')

Some attribute have naming conflicts with Python or ipywidgets. These are :code:`for`, :code:`open`, :code:`class` and
:code:`style` and must be suffixed with an underscore. For example :code:`style` becomes :code:`style_`

Vuetify:

.. code-block:: html

    <v-select style="width: 75px" label="Fruits" />

ipyvuetify:

.. jupyter-execute::

    v.Select(style_='width: 75px', label='Fruits')

In the Vuetify HTML examples you'll see attributes prefixed with a colon :code:`:`. This means the attribute is bound to
a variable or it is evaluated as an expression. If it is bound to a variable you'll see that variable being used in
other parts of the example. In ipyvuetify we use :code:`jslink()` to link these attributes. In the next section you'll
see an example of this. To look at how that variable is initialized you select the 'script' tab on a Vuetify example.

If it's an expression it's mostly used to set a List or a Dict, as is done with :code:`items` in the examples above.
This can be the same in ipyvuetify.

Reading the value
-----------------

Now we want to be able to read out the selected value. In ipywidgets this would be done by reading the :code:`value`
attribute. In Vue this is done with the :code:`v-model` directive, which is translated to Python as :code:`v_model` (
note the '_' instead of '-'). The :code:`v_model` attribute has to be explicitly set when creating the widget.

Vuetify:

.. code-block:: html

    <v-container>
        <v-select
            v-model="colorVariable"
            label="Colors"
            items="['red', 'green', 'blue']" />
        <v-chip :color="colorVariable"><v-chip>
    </v-container>

ipyvuetify:

.. jupyter-execute::

    from ipywidgets import jslink

    color_select = v.Select(
        v_model='green',
        label='Colors',
        items=['red', 'green', 'blue'])

    color_display = v.Chip()

    jslink((color_select, 'v_model'), (color_display, 'color'))

    v.Container(children=[
        color_select,
        color_display
    ])

.. note::
    ipyvuetify widgets have a :code:`value` attribute, but that's only used for setting the value, it will not change on
    interactions with the widget.

The children attribute
----------------------

Because ipyvuetify is based on HTML, which represents a GUI as a tree of elements, all widgets have an attribute
:code:`children` which is a list of widgets or strings. This way the same tree can be represented in Python. Sometimes
something you would expect to be specified as an attribute, must be specified as an item in :code:`children`, e.g. in
ipywidgets the text of a button is set with the attribute :code:`description` while in ipyvuetify the text is set with
setting an item in the :code:`children` list:

Vuetify:

.. code-block:: html

    <v-container>
        <v-btn color="primary">Click me</v-btn>
    </v-container>

ipyvuetify

.. jupyter-execute::

    v.Container(children=[
        v.Btn(color='primary', children=['Click me'])
    ])

This has the benefit of composability, e.g. the button can, in addition to text, also contain an icon:

Vuetify:

.. code-block:: html

    <v-container>
        <v-btn color="primary">
            <v-icon left>
                mdi-email-edit-outline
            </v-icon>
            Click me
        </v-btn>
    </v-container>

ipyvuetify:

.. jupyter-execute::

    v.Container(children=[
        v.Btn(color='primary', children=[
            v.Icon(left=True, children=[
                'mdi-email-edit-outline'
            ]),
            'Click me'
        ])
    ])

Events
------

Events are specified with :code:`.on_event(event_name, callback_fn)` instead of setting an attribute like in ipywidgets.

.. jupyter-execute::
    :hide-output:

    btn = v.Btn(color='primary', children=['Click me'])
    count = 0

    def on_click(widget, event, data):
        global count
        btn.children=[f'Click me {count}']
        count += 1

    btn.on_event('click', on_click)

    v.Container(children=[
        btn
    ])

The three arguments in the callback function are:

* widget: the widget the event originates from. This is useful when using the same callback for multiple widgets.
* event: the event name. This is useful when using the same callback for multiple events.
* data: data for the event. For e.g. :code:`click` of :code:`Btn` this contains which modifier keys are pressed and some
  information on the position of the mouse.

To find out what events are supported by a widget, the
`Vuetify API explorer <https://vuetifyjs.com/components/api-explorer/>`_ can be used. Search for a component and on the
left-hand side of list of attributes you will find a tab for the events.

In Vuetify events are defined as attributes with an :code:`@` prefix. The equivalent Vuetify syntax of the example above
is:

.. code-block:: html

    <v-container>
        <v-btn color="primary" @click="on_click">
            Click me {{ count }}
        </v-btn>
    </v-container>

The on_click method would be in the 'script' tab of an example and is not shown here.

Regular HTML tags
-----------------

Sometimes some regular HTML tags are needed. For this the Html widget can be used.

Vuetify:

.. code-block:: html

    <v-container>
        <h1>My heading</h1>
    </v-container>

ipyvuetify

.. jupyter-execute::

    v.Container(children=[
        v.Html(tag='h1', children=['My heading'])
    ])

Styling
-------

To visually customize widgets, the underlying CSS facilities of Vuetify are exposed. With the :code:`style_` attribute
`CSS properties <https://www.tutorialrepublic.com/css-reference/css3-properties.php>`_ can be set. Multiple CSS
properties can be set by separating them with a semicolon :code:`;`.

.. jupyter-execute::

    v.Select(label='Fruit', style_='width: 75px; opacity: 0.7')

With the :code:`class_` attribute predefined Vuetify styles can be set. Predefined styles of note are
`spacing <https://vuetifyjs.com/styles/spacing/>`_ and `colors <https://vuetifyjs.com/styles/colors/>`. More can be
found in the section 'Styles and animations' of the Vuetify documentation. Multiple classes can be applied by separating
them with a space.

Buttons without spacing:

.. jupyter-execute::

    v.Container(children=[
        v.Btn(children=[f'Button {i}']) for i in range(3)
    ])

With 2 units of margin in the x direction:

.. jupyter-execute::

    v.Container(children=[
        v.Btn(class_='mx-2', children=[f'Button {i}']) for i in range(3)
    ])

And colors:

.. jupyter-execute::

    v.Container(children=[
        v.Btn(class_=f'mx-2 indigo lighten-{i+1}', children=[f'Button {i}']) for i in range(3)
    ])

Layout (HBox/VBox alternative)
------------------------------

In ipywidgets you would layout a grid of widgets with HBox and VBox.

.. jupyter-execute::

    import ipywidgets as widgets

    widgets.HBox([
        widgets.VBox([
            widgets.Button(description="top left"),
            widgets.Button(description="bottom left"),
        ]),
        widgets.VBox([
            widgets.Button(description="top right"),
            widgets.Button(description="bottom right"),
        ]),
    ])

This can be done in ipyvuetify with the help of some classes described in
`flex helpers <https://vuetifyjs.com/styles/flex/>`_.

.. jupyter-execute::

    v.Html(tag='div', class_='d-flex flex-row', children=[
        v.Html(tag='div', class_='d-flex flex-column', children=[
            v.Btn(class_='ma-2', children=['top left']),
            v.Btn(class_='ma-2', children=['bottom left'])
        ]),
        v.Html(tag='div', class_='d-flex flex-column', children=[
            v.Btn(class_='ma-2', children=['top right']),
            v.Btn(class_='ma-2', children=['bottom right'])
        ]),
    ])

Responsive Layout
-----------------


Event modifiers
---------------

(Scoped) Slots
--------------


Summary
-------
