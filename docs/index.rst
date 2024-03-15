:html_theme.sidebar_secondary.remove:

.. raw:: html

    <!-- CSS overwrite for the landing page only -->
    <style>
    /* Make homepage wider */
    .bd-main .bd-content .bd-article-container {
        max-width: 80%;
    }
    /* hide the main title */
    h1 {display: none;}
    h2 {
        font-weight: bold;
        font-size: var(--pst-font-size-h1);
    }
    </style>

ipyvuetify: Jupyter widgets based on Vuetify UI components
==========================================================

.. raw:: html

    <div id="hero">
        <div id="hero-left">

IpyVuetify
----------

Jupyter widgets based on Vuetify UI components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Ipyvuetify** is a widget library for making modern-looking GUIs in Jupyter notebooks (`classic <https://github.com/jupyter/notebook>`__, `lab <https://github.com/jupyterlab/jupyterlab>`__, `lite <https://github.com/jupyterlite/jupyterlite>`__) and dashboards (`Voilà <https://github.com/voila-dashboards/voila>`__, `Voici <https://github.com/voila-dashboards/voici>`__). Based on the `Vuetify UI <https://v2.vuetifyjs.com/en/>`__ library, it extends the standard Jupyter widget library with additional widgets that are more customizable and composable.

.. raw:: html

    <!-- these button are only displayed in the html build -->
    <div class="homepage-button-container" style="display: none;">
        <div class="homepage-button-container-row">
            <a href="#" class="btn btn-lg sd-btn-primary">Get Started</a>
            <a href="#" class="btn btn-lg sd-btn-outline-primary">See Gallery</a>
        </div>
        <div class="homepage-button-container-row">
            <a href="#">See API Reference →</a>
        </div>
    </div>

.. raw:: html

    </div> <!-- hero-left -->
    <div id="hero-right">

.. image:: images/light-demo.gif
    :class: only-light

.. image:: images/dark-demo.gif
    :class: only-dark

.. raw:: html

    </div> <!-- hero-right -->
    </div> <!-- hero -->

.. toctree::
    :hidden:

    introduction
    installation
    usage
    advanced_usage
    template_usage
