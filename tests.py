"""
author: henry clay

date: 2/24/20

an automated testing assignment! file 2/2
"""

import unittest
import task
import math


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testCircle(self):
        pi = math.pi

        expected1 = pi
        expected2 = pi * 4
        expected3 = pi * 9
        expected0 = 0
        self.assertEqual(expected1, task.circleArea(1))
        self.assertEqual(expected2, task.circleArea(2))
        self.assertEqual(expected3, task.circleArea(3))
        self.assertEqual(expected0, task.circleArea(0))

    def testList(self):
        list1 = [1, 2]
        list2 = [1, 2, 3]
        list3 = [3]
        list4 = [1, 2, 3, 4]

        expected1 = [1, 2]
        expected2 = [1, 3]
        expected3 = [3, 3]
        expected4 = [1, 4]

        self.assertEqual(expected1, task.listFirstLast(list1))
        self.assertEqual(expected2, task.listFirstLast(list2))
        self.assertEqual(expected3, task.listFirstLast(list3))
        self.assertEqual(expected4, task.listFirstLast(list4))
