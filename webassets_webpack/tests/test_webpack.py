from unittest import TestCase

from webassets.filter import register_filter
from webassets.test import TempEnvironmentHelper
from webassets_webpack import Webpack

register_filter(Webpack)


class WebpackFilterTestCase(TempEnvironmentHelper, TestCase):

    default_files = {
        'main.js': """var odds = evens.map(v => v + 1)"""
    }

    def setUp(self):
        super(WebpackFilterTestCase, self).setup()

    def test_webpack_filter(self):
        self.env.config['WEBPACK_BIN'] = './node_modules/.bin/webpack'
        self.env.config['WEBPACK_CONFIG'] = './webpack.config.js'
        self.env.config['WEBPACK_TEMP'] = 'temp.js'

        # if not find_executable('webpack'):
        #     raise SkipTest()

        self.mkbundle('main.js', filters='webpack',
                      output='bundle.js').build()
