const appsWithComponents = new WeakSet();

export function addApp(app) {
  if (appsWithComponents.has(app)) {
    return;
  }

  appsWithComponents.add(app);
}
