const autoprefixer = require("autoprefixer");
const scopify = require("postcss-scopify");

module.exports = (ctx) => ({
  plugins: [
    autoprefixer({
      remove: false,
    }),
    scopify(".vuetify-styles"),
  ],
});
