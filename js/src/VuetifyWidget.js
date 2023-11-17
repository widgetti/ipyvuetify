import { VueModel as VueWidgetModel } from "jupyter-vue";

export class VuetifyWidgetModel extends VueWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "VuetifyWidgetModel",
        _view_name: "VuetifyView",
        _view_module: "jupyter-vuetify",
        _model_module: "jupyter-vuetify",
        _view_module_version: "3.0.0-dev.0",
        _model_module_version: "3.0.0-dev.0",
        _metadata: null,
      },
    };
  }
}

VuetifyWidgetModel.serializers = {
  ...VueWidgetModel.serializers,
};
