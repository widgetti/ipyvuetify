API reference
=============

The Python API of ipyvuetify: which widgets, traits and methods are available and what they are
called in Python. For the full details of each component, including slots, events and interactive
examples, see the `Vuetify documentation <https://vuetifyjs.com/en/components/all/>`__, every widget
page links to its Vuetify API page.

Widgets
-------

Every Vuetify component is available as a widget class in the ``ipyvuetify`` namespace, e.g.
``<v-btn>`` becomes :class:`ipyvuetify.Btn`. The traits of these classes correspond to the props of
the Vuetify component in snake_case, see :doc:`usage` for how Vuetify templates translate to Python.

.. autosummary::
    :toctree: api
    :template: autosummary/module.rst

    ipyvuetify
    ipyvuetify.extra

Reacton components
------------------

For use with `Reacton <https://reacton.solara.dev>`__ and `Solara <https://solara.dev>`__
(``solara.v``), each widget class has a component function with the same name, e.g.
:func:`ipyvuetify.components.Btn`.

.. autosummary::
    :toctree: api
    :template: autosummary/module.rst

    ipyvuetify.components
