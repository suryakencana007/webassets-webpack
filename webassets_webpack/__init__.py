from webassets.filter import ExternalTool, option

import logging

__all__ = ['Webpack']

log = logging.getLogger(__name__)


class Webpack(ExternalTool):
    """Use Webpack to bundle assets.

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
        'file_name': 'WEBPACK_OUTFILE',
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

    # def input(self, _in, out, **kw):
    #     args = [self.binary or 'webpack']
    #
    #     filename = 'main.js'
    #
    #     if self.config:
    #         args.extend(['--config', self.config])
    #
    #     if self.file_name:
    #         filename = self.file_name
    #
    #     path = kw['output_path'].split('/')
    #     _filename = path.pop(-1)
    #     path = '/'.join(path)
    #     # args.extend(['--entry', kw['source_path']])
    #     args.extend(['--output-path', path])
    #     args.extend(['--output-filename', filename])
    #
    #     self.subprocess(args, out, _in)

    def output(self, _in, out, **kw):
        args = [self.binary or 'webpack']

        filename = 'main.js'

        if self.config:
            args.extend(['--config', self.config])

        if self.file_name:
            filename = self.file_name

        self.path = kw['output_path'].split('/')
        _filename = self.path.pop(-1)
        self.path = '/'.join(self.path)
        # args.extend(['--entry', kw['source_path']])
        args.extend(['--output-path', self.path])
        args.extend(['--output-filename', filename])

        log.info('{0}/{1}'.format(self.path, filename))

        self.subprocess(args, out, _in)

    def subprocess(self, argv, out, data=None):
        ExternalTool.subprocess(argv, out, data)

        with open('{0}/{1}'.format(self.path, self.file_name), 'r+') as f:
            out.tell()
            out.seek(0)
            out.truncate(0)
            out.write(f.read())
