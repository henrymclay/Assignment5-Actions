"""
author: henry clay

date: 2/24/20

an automated testing assignment! file 2/2
"""

import unittest
import task
import math
import datetime


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

    def testDates(self):
        date1 = datetime.date(2000, 12, 30)
        date2 = datetime.date(2000, 12, 31)
        date3 = datetime.date(2001, 12, 31)
        date4 = datetime.date(2000, 11, 30)

        expected1 = datetime.timedelta(1)
        expected2 = datetime.timedelta(365)
        expected3 = datetime.timedelta(30)

        self.assertEqual(task.dateCalc(date2, date1), expected1)
        self.assertEqual(task.dateCalc(date3, date2), expected2)
        self.assertEqual(task.dateCalc(date1, date4), expected3)
