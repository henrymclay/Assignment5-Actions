"""
author: henry clay

date: 2/24/20

an automated testing assignment! file 2/2
"""

import unittest
import task

class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())