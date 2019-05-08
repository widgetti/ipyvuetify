var jupyter_vuetify = require('./index');
var base = require('@jupyter-widgets/base');

module.exports = {
  id: 'jupyter-vuetify',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      widgets.registerWidget({
          name: 'jupyter-vuetify',
          version: jupyter_vuetify.version,
          exports: jupyter_vuetify
      });
  },
  autoStart: true
};

