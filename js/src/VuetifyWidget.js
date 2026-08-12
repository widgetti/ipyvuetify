import { VueModel as VueWidgetModel } from "jupyter-vue";
import { version } from "./version";

export class VuetifyWidgetModel extends VueWidgetModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "VuetifyWidgetModel",
        _view_name: "VuetifyView",
        _view_module: "jupyter-vuetify",
        _model_module: "jupyter-vuetify",
        _view_module_version: version,
        _model_module_version: version,
        _metadata: null,
      },
    };
  }
}

VuetifyWidgetModel.serializers = {
  ...VueWidgetModel.serializers,
};
