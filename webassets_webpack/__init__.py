from contextlib import contextmanager
from tempfile import NamedTemporaryFile, TemporaryFile
import logging
from sys import version_info, platform
import os

from webassets.filter import ExternalTool

__all__ = ['Webpack']

log = logging.getLogger(__name__)

# True if we are running on Python 3.
PY3 = version_info[0] == 3


@contextmanager
def excursion(directory):
    """Context-manager that temporarily changes to a new working directory."""
    old_dir = os.getcwd()
    try:
        os.chdir(directory)
        yield
    finally:
        os.chdir(old_dir)


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

    def output(self, _in, out, **kw):
        # create a temp file
        self.temp_file = NamedTemporaryFile(suffix='.js', delete=False)
        self.temp_file.close()  # close it so windows can read it

        print(kw)
        # create temp file
        args = [self.binary or 'webpack']
        args.extend(['--config', self.config or './webpack.config.js'])

        self.path = kw['output_path'].split('/')
        self.path = self.path.pop(-1)
        # self.path = '/'.join(self.path)
        
        _tmp = self.temp_file.name.split('/')
        tmp_filename = _tmp.pop(-1)
        _tmp = '/'.join(_tmp)

        args.extend(['--output-path', _tmp])
        args.extend(['--output-filename', tmp_filename])

        self.subprocess(args, out, _in)

        with open(self.temp_file.name,
                  mode='r+') as f:
            out.tell()
            out.seek(0)
            out.truncate(0)
            if PY3:
                out.write(f.read())
            else:
                out.write(f.read().decode('utf-8'))

        os.remove(self.temp_file.name)
