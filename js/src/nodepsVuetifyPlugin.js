// nodeps.js: the host page (Solara) already has Vuetify, and shares its plugin as a global.
export const createVuetifyPlugin = () => {
  if (!window.vuetifyPlugin)
    throw new Error(
      "jupyter-vuetify nodeps.js needs the host's window.vuetifyPlugin (Solara)"
    );
  return window.vuetifyPlugin;
};
