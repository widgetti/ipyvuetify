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
        if (this.get('tag').toLowerCase().includes('script')) {
            return undefined;
        }
        return this.get('tag');
    }
}

HtmlModel.serializers = {
    ...VuetifyWidgetModel.serializers,
};
