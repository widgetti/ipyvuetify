var path = require("path");
var webpack = require("webpack");
var TerserPlugin = require("minimizer-webpack-plugin");
var version = require("./package.json").version;

// Custom webpack rules are generally the same for all webpack bundles, hence
// stored in a separate local variable.
var rules = [
  {
    test: /\.css$/,
    use: ["style-loader", "css-loader", "postcss-loader"],
  },
  {
    test: /\.(woff|woff2|eot|ttf|otf)$/,
    type: "asset/resource",
  },
];

// webpack's default minimizer (Terser, compress passes 2), plus wrap_func_args (the default
// before terser 5.43): it keeps a function passed as an argument in parentheses, so the AMD
// factory becomes define([...],((e,i,o)=>...)). V8 then compiles the factory eagerly with the
// script, off the main thread when the script streams, instead of lazily on the main thread
// when require.js calls it.
function optimization() {
  return {
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          compress: { passes: 2 },
          format: { wrap_func_args: true },
        },
      }),
    ],
  };
}

// nodeps.js uses the Vuetify plugin of the host page (Solara), and does not bundle
// Vuetify's components, directives and css. See src/nodepsVuetifyPlugin.js.
var nodepsPlugins = [
  new webpack.NormalModuleReplacementPlugin(
    /^\.\/vuetifyPlugin$/,
    "./nodepsVuetifyPlugin"
  ),
  new webpack.DefinePlugin({
    __VUETIFY_VERSION__: JSON.stringify(
      require("vuetify/package.json").version
    ),
  }),
];

module.exports = [
  {
    name: "extension",
    // Notebook extension
    //
    // This bundle only contains the part of the JavaScript that is run on
    // load of the notebook. This section generally only performs
    // some configuration for requirejs, and provides the legacy
    // "load_ipython_extension" function which is required for any notebook
    // extension.
    //
    entry: "./lib/extension.js",
    output: {
      filename: "extension.js",
      path: path.resolve(
        __dirname,
        "..",
        "prefix",
        "share",
        "jupyter",
        "nbextensions",
        "jupyter-vuetify"
      ),
      libraryTarget: "amd",
    },
    mode: "production",
    optimization: optimization(),
  },
  {
    name: "notebook",
    // Bundle for the notebook containing the custom widget views and models
    //
    // This bundle contains the implementation for the custom widget views and
    // custom widget.
    // It must be an amd module
    //
    entry: "./lib/notebook.js",
    output: {
      filename: "index.js",
      path: path.resolve(
        __dirname,
        "..",
        "prefix",
        "share",
        "jupyter",
        "nbextensions",
        "jupyter-vuetify"
      ),
      libraryTarget: "amd",
    },
    devtool: "source-map",
    module: {
      rules: rules,
    },
    externals: ["@jupyter-widgets/base", "@jupyterlab/apputils", "jupyter-vue"],
    resolve: {
      alias: {
        vue$: path.resolve(__dirname, "lib", "vue_alias"),
      },
    },
    mode: "production",
    optimization: optimization(),
    performance: {
      maxEntrypointSize: 1400000,
      maxAssetSize: 1400000,
    },
  },
  {
    name: "nodeps-notebook",
    entry: "./lib/nodeps.js",
    output: {
      filename: "nodeps.js",
      path: path.resolve(
        __dirname,
        "..",
        "prefix",
        "share",
        "jupyter",
        "nbextensions",
        "jupyter-vuetify"
      ),
      libraryTarget: "amd",
    },
    devtool: "source-map",
    module: {
      rules: rules,
    },
    resolve: {
      alias: {
        vue$: path.resolve(__dirname, "lib", "vue_alias"),
      },
    },
    externals: [
      "@jupyter-widgets/base",
      "@jupyterlab/apputils",
      "jupyter-vue",
      "material-design-icons-iconfont",
      "typeface-roboto",
      "@mdi/font",
      "vuetify",
    ],
    plugins: nodepsPlugins,
    mode: "production",
    optimization: optimization(),
  },
  {
    name: "nodeps-embed",
    entry: "./lib/nodepsEmbed.js",
    output: {
      filename: "nodeps.js",
      path: path.resolve(__dirname, "dist"),
      libraryTarget: "amd",
      publicPath: "https://unpkg.com/jupyter-vuetify@" + version + "/dist/",
    },
    devtool: "source-map",
    module: {
      rules: rules,
    },
    resolve: {
      alias: {
        vue$: path.resolve(__dirname, "lib", "vue_alias"),
      },
    },
    externals: [
      "@jupyter-widgets/base",
      "@jupyterlab/apputils",
      "jupyter-vue",
      "material-design-icons-iconfont",
      "typeface-roboto",
      "@mdi/font",
      "vuetify",
    ],
    plugins: nodepsPlugins,
    mode: "production",
    optimization: optimization(),
  },
  {
    name: "embed",
    // Embeddable jupyter-vuetify bundle
    //
    // This bundle is generally almost identical to the notebook bundle
    // containing the custom widget views and models.
    //
    // The only difference is in the configuration of the webpack public path
    // for the static assets.
    //
    // It will be automatically distributed by unpkg to work with the static
    // widget embedder.
    //
    // The target bundle is always `dist/index.js`, which is the path required
    // by the custom widget embedder.
    //
    entry: "./lib/embed.js",
    output: {
      filename: "index.js",
      path: path.resolve(__dirname, "dist"),
      libraryTarget: "amd",
      publicPath: "https://unpkg.com/jupyter-vuetify@" + version + "/dist/",
    },
    devtool: "source-map",
    module: {
      rules,
    },
    externals: ["@jupyter-widgets/base", "@jupyterlab/apputils", "jupyter-vue"],
    resolve: {
      alias: {
        vue$: path.resolve(__dirname, "lib", "vue_alias"),
      },
    },
    mode: "production",
    optimization: optimization(),
    performance: {
      maxEntrypointSize: 1400000,
      maxAssetSize: 1400000,
    },
  },
];
