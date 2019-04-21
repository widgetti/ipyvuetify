/**
 * Workaround for: https://github.com/webpack/webpack/issues/985. Not using npm link here, but the same problem occurs
 * with 'file:../vuetify/packages/vuetify' in package.json.
 */

const fs = require('fs-extra');
['dist', 'src', 'types', 'es5', 'lib']
    .forEach(dir =>
        fs.copySync(`${__dirname}/../vuetify/packages/vuetify/${dir}`, `node_modules/vuetify/${dir}`));
