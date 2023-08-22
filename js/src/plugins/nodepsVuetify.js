// import vuetify from 'vuetify';

/* The import above would break voila-vuetify and voila-embed users, so use the workaround below
 * until all users have upgraded to Voila-vuetify > 0.2.2 and voila-embed > 2020-02-11, or
 * ipyvuetify bumps a major version */
const vuetify =
  window.app && window.app.$vuetify && window.app.$options.vuetify;

export default vuetify;
