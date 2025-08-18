module.exports = {
    env: {
      es2021: true,
      node: true,
      jest: true
    },
    extends: ['eslint:recommended'],
    parserOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module'
    },
    rules: {
      'no-var': 'error',
      'prefer-const': 'error'
    }
  };
  