function scriptExists(fingerprint) {
  return [].slice
    .call(document.getElementsByTagName("script"))
    .map((e) => e.src)
    .find((e) => e.includes(fingerprint));
}

export function getLabContainer() {
  return (
    scriptExists("/lab/static/main.") &&
    document.querySelector("div#main.jp-ApplicationShell")
  );
}

export function getNotebookContainer() {
  return (
    scriptExists("/static/notebook/js/main.min.js") &&
    document.querySelector("body.notebook_app div#site")
  );
}

export function getVoilaContainer() {
  return (
    scriptExists("/voila/static/main.js") &&
    document.querySelector("div#notebook")
  );
}

export function getContainer() {
  return getLabContainer() || getNotebookContainer() || getVoilaContainer();
}
