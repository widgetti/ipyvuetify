const localVuetify = new URL("_static/jupyter-vuetify/index", document.baseURI)
  .href;

require.config({
  paths: {
    "jupyter-vue":
      "https://cdn.jsdelivr.net/npm/jupyter-vue@3.0.0-alpha.5/dist/index",
    "jupyter-vuetify": localVuetify,
  },
});

const script = document.createElement("script");
script.src =
  "https://cdn.jsdelivr.net/npm/@jupyter-widgets/html-manager@^1.0.1/dist/embed-amd.js";
document.head.appendChild(script);
