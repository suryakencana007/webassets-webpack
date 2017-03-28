from unittest import TestCase
from distutils.spawn import find_executable
from nose import SkipTest


from webassets.filter import register_filter
from webassets.test import TempEnvironmentHelper

from webassets_webpack import Webpack

register_filter(Webpack)


class WebpackFilterTestCase(TempEnvironmentHelper, TestCase):

    default_files = {
        'main.js': """
            import _ from 'lodash';

            function component () {
              var element = document.createElement('div');

              /* lodash is required for the next line to work */
              element.innerHTML = _.join(['Hello','webpack'], ' ');

              return element;
            }

            document.body.appendChild(component());
        """
    }

    def setUp(self):
        super(WebpackFilterTestCase, self).setup()

    def test_webpack_filter(self):
        self.env.config['WEBPACK_BIN'] = './node_modules/.bin/webpack'
        self.env.config['WEBPACK_CONFIG'] = './webpack.config.js'
        self.env.config['WEBPACK_OUTFILE'] = 'debug.js'

        # if not find_executable('webpack'):
        #     raise SkipTest()

        self.mkbundle('main.js', filters='webpack',
                      output='bundle.js').build()
