from unittest import TestCase

from webassets.filter import register_filter
from webassets.test import TempEnvironmentHelper

from webassets_webpack import Webpack


register_filter(Webpack)


class WebpackFilterTestCase(TempEnvironmentHelper, TestCase):

    default_files = {
        'main.js': """var x = (p) => { return false; };"""
    }

    def setUp(self):
        super(WebpackFilterTestCase, self).setup()

    def test_webpack_filter(self):
        self.mkbundle('main.js', filters='webpack',
                      output='bundle.js').build()
        self.get('bundle.js')
        # assert "var x = function x" in self.get('bundle.js')
