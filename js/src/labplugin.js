const base = require('@jupyter-widgets/base');
const apputils = require('@jupyterlab/apputils');

const jupyterVuetify = require('./index');

module.exports = {
    id: 'jupyter-vuetify',
    requires: [base.IJupyterWidgetRegistry],
    optional: [apputils.IThemeManager],
    activate(app, widgets, themeManager) {
        jupyterVuetify.ThemeModel.themeManager = themeManager
        widgets.registerWidget({
            name: 'jupyter-vuetify',
            version: jupyterVuetify.version,
            exports: jupyterVuetify,
        });
    },
    autoStart: true,
};
