from webassets.filter import ExternalTool, option

__all__ = ['Webpack']


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
			Passed straight through to ``webpack --config`` to specify which webpack
      config to use

  """

	name = 'webpack'
	max_debug_level = None
	options = {
	'binary': 'WEBPACK_BIN',
	'config': 'WEBPACK_CONFIG',
  'run_in_debug': 'WEBPACK_RUN_IN_DEBUG',
	}

	def setup(self):
		super(Webpack, self).setup()
		if self.run_in_debug is False:
			# Disable running in debug mode for this instance
			self.max_debug_level = False

	def input(self, _in, out, **kw):
		args = [self.binary or 'webpack']

		if self.config:
			args.extend(('--config', self.config))

			return self.subprocess(args, out, _in)