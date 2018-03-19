from setuptools import setup, find_packages
import os

version = '1.3.0'
maintainer = 'Thomas Buchberger'

tests_require = [
    'ftw.builder',
    'ftw.testbrowser',
    'plone.app.testing',
    'plone.testing',
    'unittest2',
    'zope.app.testing',
]

setup(name='ftw.datepicker',
      version=version,
      description="A z3c.form datepicker widget (Maintainer %s)" % maintainer,

      long_description=open("README.rst").read() + "\n" + \
                       open(os.path.join("docs", "HISTORY.txt")).read(),

      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.1',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        ],

      keywords='ftw 4teamwork widget date picker',
      author='%s, 4teamwork AG' % maintainer,
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='https://github.com/4teamwork/ftw.datepicker',

      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'Plone',
          'collective.js.jqueryui',
          'ftw.upgrade',
          'plone.app.z3cform>=0.5.1',
          'plone.z3cform',
          'setuptools',
          'z3c.form',
      ],

      extras_require=dict(
          tests=tests_require,
          ),
      tests_require=tests_require,

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
