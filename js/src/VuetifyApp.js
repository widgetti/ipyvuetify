import { VDataTable } from "vuetify/labs/VDataTable";

const appsWithComponents = new WeakSet();

export function addApp(app) {
  if (appsWithComponents.has(app)) {
    return;
  }

  app.component("VDataTable", VDataTable);
  appsWithComponents.add(app);
}
