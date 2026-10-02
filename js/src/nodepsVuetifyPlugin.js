/* nodeps.js (Solara): the host page already has Vuetify (components, directives and
 * unscoped css) and exposes its plugin as the global vuetifyPlugin. Using it avoids a
 * second Vuetify copy, and Lumino-hosted views get the host's theme.
 */
import { version as hostVersion } from "vuetify";

/* global __VUETIFY_VERSION__ */
const builtForVersion = __VUETIFY_VERSION__;

function minorVersion(version) {
  const [major, minor] = String(version).split(".").map(Number);
  return major * 1000 + minor;
}

export function createVuetifyPlugin() {
  const plugin = globalThis.vuetifyPlugin;
  if (!plugin) {
    throw new Error(
      "jupyter-vuetify nodeps.js needs the host's vuetifyPlugin (Solara with Vue 3)"
    );
  }
  if (
    hostVersion &&
    minorVersion(hostVersion) < minorVersion(builtForVersion)
  ) {
    // Solara before 1.61 has Vuetify 3.3: newer components (VDatePicker) do not render
    console.warn(
      `jupyter-vuetify nodeps.js uses the host's Vuetify ${hostVersion}, but is built for Vuetify ${builtForVersion}. ` +
        "Components that the older Vuetify does not have do not render. Upgrade the host (Solara 1.61 or later)."
    );
  }
  return plugin;
}
