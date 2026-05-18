#!/bin/bash
if ! test -d "vuetify"; then
  git clone https://github.com/vuetifyjs/vuetify.git
  cd vuetify
  git checkout v3.3.22
  npm install -g yarn
  yarn
  yarn build
  cd ..
fi
python generate_code.py
pre-commit run  --files ../ipyvuetify/generated.py ../js/src/Widgets.js
