import './public-path';
import 'typeface-roboto';
import 'material-design-icons-iconfont/dist/material-design-icons.css';
import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import './styles.css';

Vue.use(Vuetify, {
    iconfont: 'md'
});

export * from './helpers';
export * from './generated';
export { HtmlModel } from './Html';
export { VuetifyTemplateModel } from './VuetifyTemplate';
export { VuetifyTemplateView } from './VuetifyTemplateView';
