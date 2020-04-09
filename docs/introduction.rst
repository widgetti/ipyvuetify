Introduction
============

Ipyvuetify is a widget library for making modern looking GUI's in Jupyter notebooks (classic and lab) and dashboards
(`Voilà <https://voila.readthedocs.io/en/stable/using.html>`_). It's based on the `Google material design philosophy
<https://material.io/design/introduction>`_ best known from the Android user interface.

A large set of widgets is provided with many widgets having multiple variants. a few of which are displayed below.
[TODO: fix CSS collisions with rtd_theme]

.. jupyter-execute:: showcase.py
    :hide-code:

Many widgets are composable:
<TODO: Composability example>

There is support for responsive layouts, which are not that useful in a notebook because of the fixed width, but come in
handy when making dashboards with Voilà, making your dashboard usable on tablets and phones.
<TODO: responsive example?>

When comparing ipyvuetify to `ipywidgets <https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20Basics.html>`_,
the standard widget library of Jupyter, ipyvuetify has a lot more widgets which are also more customizable and
composable at the expense of a bit more verbosity in the source code.

Ipyvuetify uses the machinery of `ipywidgets <https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20Basics.html>`_
as a base, but has different conventions for the API. This is mainly due to the fact the Python API is generated from
the JavaScript library it is based on: `Vuetify <https://vuetifyjs.com/>`_. This exposes the full power of Vuetify and
allows us to rely on the extensive documentation and examples of it. Generating code and relying on documentation from
the underlying library allowed us to expose a lot of widgets to Jupyter in a relatively short amount of time.

In :doc:`usage` al concepts and how they differ from ipywidgets will be explained and supported by examples.

To explore which widgets are available and how to use them we defer to the
`Vuetify documentation <https://vuetifyjs.com/nl-NL/components/buttons/>`_. You can browse examples on the left-hand
side and see the source code by clicking on '< >' of the example on the top right-hand side of the example. By reading
:doc:`usage` and :doc:`translating_vuetify` you will be able to translate the examples to ipyvuetify.
