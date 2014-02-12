import unittest

from zope.testing import doctest

from z3c.form import testing


def test_suite():
    return unittest.TestSuite((
        doctest.DocFileSuite(
            '../converter.txt',
            setUp=testing.setUp, tearDown=testing.tearDown,
            optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,
            ),
        ))
