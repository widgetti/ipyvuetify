#!/bin/bash
if ! test -d "vuetify"; then
  git clone https://github.com/vuetifyjs/vuetify.git
fi
cd vuetify
git checkout v3.12.9
npm install -g pnpm@10.26.1
pnpm install --frozen-lockfile
pnpm --filter vuetify build
pnpm --filter @vuetify/api-generator exec node --no-warnings src/index.ts --skip-composables --skip-directives
cd ..
python generate_code.py
pre-commit run  --files ../ipyvuetify/generated.py ../js/src/Widgets.js
