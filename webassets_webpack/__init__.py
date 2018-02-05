from tempfile import NamedTemporaryFile
import logging
import sys

from webassets.filter import ExternalTool

__all__ = ['Webpack']

log = logging.getLogger(__name__)

# True if we are running on Python 3.
PY3 = sys.version_info[0] == 3


class Webpack(ExternalTool):
    """
    Use Webpack to bundle assets.

    Requires the Webpack executable to be available externally. You can
    install it using `Node Package Manager <http://npmjs.org/>`_::

    $ npm install webpack --save-dev

    Supported configuration options:

    WEBPACK_BIN
    The path to the Webpack binary. If not set, assumes ``Webpack``
    is in the system path.

    WEBPACK_CONFIG
    Passed straight through to ``webpack --config``
    to specify which webpack config to use
    """

    name = 'webpack'
    max_debug_level = None
    options = {
        'binary': 'WEBPACK_BIN',
        'config': 'WEBPACK_CONFIG',
        'run_in_debug': 'WEBPACK_RUN_IN_DEBUG',
    }

    def __init__(self):
        super(Webpack, self).__init__()
        self.path = ''

    def setup(self):
        super(Webpack, self).setup()
        if self.run_in_debug is False:
            # Disable running in debug mode for this instance
            self.max_debug_level = False

    def open(self, out, source_path, **kw):
        log.info(source_path)

    def output(self, _in, out, **kw):
        args = [self.binary or 'webpack']

        if self.config:
            args.extend(['--config', self.config])

        with NamedTemporaryFile("r", suffix=".js") as temp_file:

            self.path = kw['output_path'].split('/')
            self.path.pop(-1)

            self.path = '/'.join(self.path)
            # args.extend(['--entry', kw['source_path']])
            args.extend(['--output-path', self.path])
            args.extend(['--output-filename', temp_file])

            log.debug(temp_file.name)

            out.tell()
            out.seek(0)
            out.truncate(0)
            if PY3:
                out.write(temp_file.read())
            else:
                out.write(temp_file.read().decode('utf-8'))
