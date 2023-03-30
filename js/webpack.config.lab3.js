var path = require("path");

module.exports = {
  resolve: {
    alias: {
      vue$: path.resolve(__dirname, "lib", "vue_alias"),
    },
  },
};
