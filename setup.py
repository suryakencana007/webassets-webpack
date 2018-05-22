# -*- coding: utf-8 -*-
"""
Webpack filter for webassets
-------------------------------

.. image:: https://travis-ci.org/suryakencana/webassets-webpack.svg?branch=master
    :target: https://travis-ci.org/suryakencana/webassets-webpack


Filter for for compiling assets using `Webpack <https://webpack.js.org>`_ and
`webassets <http://webassets.readthedocs.org>`_.

Basic usage
```````````

.. code:: python

    from webassets.filter import register_filter
    from webassets_browserify import Webpack

    register_filter(Webpack)


Usage with Django
`````````````````

This requires `django-assets <http://django-assets.readthedocs.org>`_.

.. code:: python

    from django_assets import Bundle, register
    from webassets.filter import register_filter
    from webassets_webpack import Webpack

    register_filter(Webpack)

    js = Bundle('js/main.js', filters='webpack', output='bundle.js',
                depends='js/**/*.js')
    register('js_all', js)

"""
from setuptools import setup, find_packages


setup(name='webassets-webpack',
      version='0.1.4',
      description='Webpack filter for webassets',
      long_description=__doc__,
      author='Nanang Suryadi',
      author_email='nanang.jobs@gmail.com',
      license='MIT',
      url='https://github.com/suryakencana/webassets-webpack',
      download_url='https://github.com/suryakencana/webassets-webpack/archive/0.1.0.tar.gz',
      packages=find_packages(),
      keywords=['webpack', 'webassets', 'django assets', 'pyramid assets'],
      install_requires=['webassets'],
      test_suite='webassets_webpack.tests',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
      ])
