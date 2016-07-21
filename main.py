import unittest
from test import TestDoubanBookSearchAPI

if __name__ == "__main__":
    s = unittest.TestSuite()
    s.addTest(TestDoubanBookSearchAPI())
    unittest.main()