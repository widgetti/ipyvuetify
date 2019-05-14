import { VuetifyWidgetModel } from './generated/VuetifyWidget';

export
class HtmlModel extends VuetifyWidgetModel {
    defaults() {
        return {
            ...super.defaults(),
            ...{
                _model_name: 'HtmlModel',
                tag: null,
            },
        };
    }

    getVuetifyTag() { // eslint-disable-line class-methods-use-this
        return 'html';
    }
}

HtmlModel.serializers = {
    ...VuetifyWidgetModel.serializers,
};
