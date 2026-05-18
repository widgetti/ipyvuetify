var path = require("path");

var rules = [
  {
    test: /\.css$/,
    use: ["postcss-loader"],
  },
];

module.exports = {
  resolve: {
    alias: {
      vue$: path.resolve(__dirname, "lib", "vue_alias"),
    },
  },
  module: {
    rules: rules,
  },
};
