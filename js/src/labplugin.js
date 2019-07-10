const base = require('@jupyter-widgets/base');
const jupyterVuetify = require('./index');

module.exports = {
    id: 'jupyter-vuetify',
    requires: [base.IJupyterWidgetRegistry],
    activate(app, widgets) {
        widgets.registerWidget({
            name: 'jupyter-vuetify',
            version: jupyterVuetify.version,
            exports: jupyterVuetify,
        });
    },
    autoStart: true,
};
