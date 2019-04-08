import {
    WidgetModel, DOMWidgetModel,
    WidgetView, DOMWidgetView,
    unpack_models
} from '@jupyter-widgets/base';

export class VuetifyTemplateModel extends DOMWidgetModel {

    defaults() {
        return {
            ...super.defaults(), ...{
                _model_name: "VuetifyTemplateModel",
                _view_name: "VuetifyTemplateView",
                _view_module: "jupyter-vuetify",
                _model_module: "jupyter-vuetify",
                _view_module_version: "0.1.0",
                _model_module_version: "0.1.0",
                template: null,
                events: null,
            }
        };
    }
}

VuetifyTemplateModel.serializers = {
    ...DOMWidgetModel.serializers,
    components: {deserialize: unpack_models},
};
