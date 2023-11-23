# upgrading these packages fails when using yarn cli
for path in ["vuetify/packages/vuetify/package.json", "vuetify/packages/docs/package.json"]:
    with open(path, "r") as f:
        file_contents = f.read()

    with open(path, "w") as f:
        f.write(file_contents.replace('"fibers": "^4.0.1"', '"fibers": "^5"'))
