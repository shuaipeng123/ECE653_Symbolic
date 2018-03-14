import sys
import unittest
import os

if __name__ == '__main__':

    name = 'a2q3.puzzle_tests'
    suite = unittest.defaultTestLoader.loadTestsFromNames ([name])
    result = unittest.TextTestRunner().run (suite)
