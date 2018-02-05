# Webpack filter for webassets [![Build Status](https://travis-ci.org/suryakencana/webassets-webpack.svg?branch=master)](https://travis-ci.org/suryakencana/webassets-webpack)


Filter for for compiling assets using [Webpack](ttps://webpack.js.org) and [webassets](http://webassets.readthedocs.org). Requires Python 2.7 or Python 3.3 and newer.

## Installation
```bash
pip install webassets_webpack
```

## Basic usage

```python
from webassets.filter import register_filter
from webassets_webpack import Webpack

register_filter(Webpack)
```

## Usage with Django

This requires [django-assets](http://django-assets.readthedocs.org).

```python
from django_assets import Bundle, register
from webassets.filter import register_filter
from webassets_webpack import Webpack

register_filter(Webpack)

js = Bundle('js/main.js', filters='webpack', output='bundle.js',
            depends='js/**/*.js')
register('js_all', js)
```

## Options

##### WEBPACK_BIN

The path to the Webpack binary. If not set, assumes ``Webpack`` is in the system path.

##### WEBPACK_CONFIG

Passed straight through to ``webpack --config`` to specify which webpack
      config to use

##### EXAMPLE

file assets.yaml

```yaml
es-webpack:
    config:
        WEBPACK_BIN: ./node_modules/.bin/webpack
        WEBPACK_CONFIG: ./webpack.config.js
        WEBPACK_TEMP: temp.js
    filters: webpack
    output: b:public/bundle.%(version)s.js
    contents:
        - jsx/index.js
    
```
 
file webpack.config.js
 
```javascript
    
var webpack = require('webpack');
var path = require('path');
var node_modules_dir = path.join(__dirname, 'node_modules');


module.exports = {
    entry: path.resolve(__dirname, 'b/assets/jsx/todo/index.js'),
    module: {
        rules: [
            {
                test: /\.js$/,
                use: [
                    'babel-loader',
                ],
                exclude: node_modules_dir,
                include: path.join(__dirname, 'b/assets/jsx/todo')
            },
        ]
    },
    plugins: [
        // build optimization plugins
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false,
                drop_console: false,
            }
        })
    ]
}

```

code pyhton

```python
from webassets.filter import register_filter
from webassets_webpack import Webpack

register_filter(Webpack)

for url in request.web_env['es-webpack'].urls():
    h.tags.javascript_link(static(url))
    
```

## License

MIT
