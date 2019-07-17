import 'typeface-roboto';
import 'material-design-icons-iconfont/dist/material-design-icons.css';
import Vue from 'vue';
import Vuetify from '@mariobuikhuizen/vuetify';
import '@mariobuikhuizen/vuetify/dist/vuetify.min.css';
import './styles.css';

Vue.use(Vuetify, {
    iconfont: 'md',
});

export { VuetifyView } from './VuetifyView';
export * from './generated';
export { HtmlModel } from './Html';
export { VuetifyTemplateModel } from './VuetifyTemplate';

export const { version } = require('../package.json'); // eslint-disable-line global-require
