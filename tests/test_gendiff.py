import re
from gendiff.scripts.gendiff import test_for_test, generate_diff

def test_test_for_test():
    result = 1234
    assert result == test_for_test()

def test_generate_diff():
    print('ssmthng')
