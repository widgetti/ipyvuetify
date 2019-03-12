#!/bin/bash
js/node_modules/.bin/widgetgen -p json -o js/lib -t js/gen-source/es6-template.njk js/gen-source/ipyvuetify.json es6
js/node_modules/.bin/widgetgen -p json -o ipyvuetify -t js/gen-source/python.njk js/gen-source/ipyvuetify.json python
echo -e "export * from './helpers';\n$(cat js/lib/index.js)" > js/lib/index.js
