/* eslint camelcase: off */
import { HtmlModel as VueHtmlModel } from "jupyter-vue";

export class HtmlModel extends VueHtmlModel {
  defaults() {
    return {
      ...super.defaults(),
      ...{
        _model_name: "HtmlModel",
        _view_name: "VuetifyView",
        _view_module: "jupyter-vuetify",
        _model_module: "jupyter-vuetify",
        _view_module_version: "3.0.0-dev.0",
        _model_module_version: "3.0.0-dev.0",
      },
    };
  }
}

HtmlModel.serializers = {
  ...VueHtmlModel.serializers,
};
