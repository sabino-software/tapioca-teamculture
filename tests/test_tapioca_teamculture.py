# coding: utf-8

import unittest

from tapioca_teamculture import TeamCulture


class TestTapiocaTeamCulture(unittest.TestCase):

    def setUp(self):
        self.wrapper = TeamCulture()


if __name__ == '__main__':
    unittest.main()
