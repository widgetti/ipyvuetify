/**
 *  Setup notebook base URL
 *
 * Some static assets may be required by the custom widget javascript. The base
 * url for the notebook is not known at build time and is therefore computed
 * dynamically.
 */

const baseUrl = document.querySelector("body").getAttribute("data-base-url");
__webpack_public_path__ = `${baseUrl}nbextensions/jupyter-vuetify/`; // eslint-disable-line no-undef
