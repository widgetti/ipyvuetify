const configs = require("./webpack.config");

module.exports = configs.filter((config) => config.name === "embed");
