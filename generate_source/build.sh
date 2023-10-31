#!/bin/bash
if ! test -d "vuetify"; then
  git clone https://github.com/vuetifyjs/vuetify.git
  cd vuetify
  git checkout v3.3.22
  pm install -g yarn
  yarn
  yarn build
  cd ..
fi
python generate_code.py
pre-commit run  --files ../ipyvuetify/vuetify_widgets.py ../js/src/Widgets.js
