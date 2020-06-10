from test_suite import TestSuite as test
from day_07 import *

def run_tests():
    test_list = ['a', 'b', 'c', 'd']
    test.assert_equals(reverse_list(test_list), ['d', 'c', 'b', 'a'])

run_tests()