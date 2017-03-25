# -*- coding: utf-8 -*-

from .context import cup_holder

import unittest


class WalkTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_walk_forward(self):
        assert True


if __name__ == '__main__':
    unittest.main()
