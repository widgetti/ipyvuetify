var jupyter-vuetify = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'jupyter-vuetify',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'jupyter-vuetify',
          version: jupyter-vuetify.version,
          exports: jupyter-vuetify
      });
  },
  autoStart: true
};

