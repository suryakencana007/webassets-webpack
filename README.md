# Webpack filter for webassets [![Build Status](https://travis-ci.org/suryakencana/webassets-webpack.svg?branch=master)](https://travis-ci.org/suryakencana/webassets-webpack)


Filter for for compiling assets using [Webpack](ttps://webpack.js.org) and [webassets](http://webassets.readthedocs.org). Requires Python 2.7 or Python 3.3 and newer.

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

he path to the Webpack binary. If not set, assumes ``Webpack`` is in the system path.

##### WEBPACK_CONFIG

Passed straight through to ``webpack --config`` to specify which webpack
      config to use

## License

MIT
