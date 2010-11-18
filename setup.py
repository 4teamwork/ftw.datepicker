from setuptools import setup, find_packages
import os

version = open('ftw/datepicker/version.txt').read().strip()
maintainer = 'Thomas Buchberger'

tests_require = [
	'z3c.form[test]',
	'collective.testcaselayer',
            ]

setup(name='ftw.datepicker',
      version=version,
      description="A z3c.form datepicker widget (Maintainer %s)" % maintainer,
      long_description=open("README.txt").read() + "\n" + \
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='ftw 4teamwork widget date picker',
      author='%s, 4teamwork GmbH' % maintainer,
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='http://psc.4teamwork.ch/dist/ftw-datepicker/',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'z3c.form',
          'setuptools',
          'plone.z3cform',
          'plone.app.z3cform>=0.5.0',
          'collective.js.jqueryui',
          # -*- Extra requirements: -*-
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
