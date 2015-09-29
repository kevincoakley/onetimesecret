from os.path import dirname
import unittest


def load_tests():
    return unittest.defaultTestLoader.discover(dirname(__file__))
