module.exports = {
  env: {
    browser: true,
    es6: true,
  },
  extends: 'airbnb-base',
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: [
    'vue',
  ],
  rules: {
    'indent': ['error', 4, { 'SwitchCase': 1 }],
    'import/prefer-default-export': 'off',
    'camelcase': ["error", {allow: ['__webpack_public_path__', 'load_ipython_extension', '_model_name']}],
    'no-underscore-dangle': 'off',
    'class-methods-use-this': 'off',
    'no-use-before-define': 'off'
},
};
