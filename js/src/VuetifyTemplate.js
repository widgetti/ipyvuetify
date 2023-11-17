/* eslint camelcase: off */
import { VueTemplateModel } from "jupyter-vue";

export class VuetifyTemplateModel extends VueTemplateModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "VuetifyTemplateModel",
        _view_name: "VuetifyView",
        _view_module: "jupyter-vuetify",
        _model_module: "jupyter-vuetify",
        _view_module_version: "3.0.0-dev.0",
        _model_module_version: "3.0.0-dev.0",
      },
    };
  }
}

VuetifyTemplateModel.serializers = {
  ...VueTemplateModel.serializers,
};
