#!/bin/bash

#Note!: this will only work on node <=14

# use script directory as working directory
cd "${0%/*}"

rm -rf vuetify
git clone --branch v2.2.26 --depth 1 https://github.com/vuetifyjs/vuetify.git
npm install -g yarn
python patch_vuetify_build.py
(cd vuetify && yarn --ignore-optional && yarn build)

node -e 'console.log(JSON.stringify(require("./vuetify/packages/api-generator/dist/api.js"), null, 2))' > vuetify_api.json
pre-commit run --files vuetify_api.json
