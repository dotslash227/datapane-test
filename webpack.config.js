var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry:{
  myapp: './reactjs/app/myapp',
  csv: './reactjs/app/csv'

},

output: {
      path: path.resolve('./static/bundles/'),
      filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],
  module: {
    rules: [
      { test: /\.js$|jsx/, use: 'babel-loader', exclude: /node_modules/ }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  }

};