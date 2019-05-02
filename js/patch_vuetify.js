/**
 * Workaround for: https://github.com/webpack/webpack/issues/985. Not using npm link here, but the same problem occurs
 * with 'file:../vuetify/packages/vuetify' in package.json.
 */

const fs = require('fs-extra');
['dist', 'src', 'types', 'es5', 'lib']
    .forEach(dir =>
        fs.copySync(`${__dirname}/../vuetify/packages/vuetify/${dir}`, `node_modules/vuetify/${dir}`));

/**
 * Workaround to prefix vuetify css selectors.
 *
 * I've tried to import the .styl files under a prefix like suggested in:
 * https://stackoverflow.com/questions/54201469/how-to-isolate-vuetify-global-styles.
 *
 * But this produces a .css file with rules in a different order, which is significant for some rules.
 */

const cssPath = 'node_modules/vuetify/dist';
const source = `${cssPath}/vuetify.css`;
const destination = `${cssPath}/vuetify.prefixed.css`;
const prefix = '.vuetify-styles';

const data = fs.readFileSync(source).toString('utf8');
const result = data.replace(/(?=^[^@|^%]+$)( *)(.*)([{|,])$/gm, `$1${prefix} $2$3`);
fs.writeFileSync(destination, result);
