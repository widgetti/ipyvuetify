#!/bin/bash
DST_JS=js/lib/generated
DST_PYTHON=ipyvuetify/generated
WIDGET_GEN_SCHEMA=js/gen-source/widget_gen_schema.json

rm -rf $DST_JS
mkdir -p $DST_JS
js/node_modules/.bin/widgetgen -p json -o "$DST_JS" -t js/gen-source/es6-template.njk $WIDGET_GEN_SCHEMA es6

rm -rf $DST_PYTHON
mkdir -p $DST_PYTHON
js/node_modules/.bin/widgetgen -p json -o "$DST_PYTHON" -t js/gen-source/python.njk $WIDGET_GEN_SCHEMA python
sed -i -e 's/v_model = Any(Undefined).tag(sync=True)/v_model = Any("!!disabled!!").tag(sync=True)/g' ipyvuetify/generated/VuetifyWidget.py

