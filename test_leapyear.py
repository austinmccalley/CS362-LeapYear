from leapyear import leapYear
import unittest


class test_LeapYear(unittest.TestCase):

  def test2020(self):
    self.assertTrue(leapYear('2020'))

  def test2019(self):
    self.assertFalse(leapYear('2019'))

  def testEdge(self):
    self.assertTrue(leapYear('0'))

  def testNonYear(self):
    self.assertFalse(leapYear('abc'))

  def test2000(self):
    self.assertTrue(leapYear('2000'))

  def test1972(self):
    self.assertTrue(leapYear('1972'))

  def test1974(self):
    self.assertFalse(leapYear('1974'))

if __name__ == '__main__':
  unittest.main()