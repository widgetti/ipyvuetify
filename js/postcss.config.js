const autoprefixer = require("autoprefixer");
const scopify = require("postcss-scopify");

module.exports = (ctx) => {
  const plugins = [
    autoprefixer({
      remove: false,
    }),
  ];
  // There are styles that should be global in styles.css, so we skip it
  if (!ctx.file.endsWith("ipyvuetify/js/lib/styles.css")) {
    plugins.push(
      scopify({
        scope: ":where(.vuetify-styles)",
      })
    );
  }

  return {
    plugins,
  };
};
