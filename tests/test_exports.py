"""
Test package exports
"""

import unittest

from some.package import logging


class TestExports(unittest.TestCase):  # pylint: disable=missing-class-docstring

    def setUp(self):  # pylint: disable=missing-function-docstring
        self._logging_members = dir(logging)

    def test_getLogger(self):  # pylint: disable=missing-function-docstring,invalid-name
        self.assertIn('getLogger', self._logging_members)


if __name__ == '__main__':
    unittest.main()
