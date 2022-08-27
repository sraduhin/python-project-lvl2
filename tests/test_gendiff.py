from gendiff.comparer import generate_diff
from gendiff.parser.parser import parser
import pytest


def test_generate_diff_json():
    pathfile1 = 'tests/fixtures/file1.json'
    pathfile2 = 'tests/fixtures/file2.json'
    with open(pathfile1, 'r'):
        with open(pathfile2, 'r'):
            with open('tests/fixtures/result_json', 'r') as result:
                result = result.read()
                assert generate_diff(pathfile1, pathfile2) == result


def test_generate_diff_yml():
    pathfile1 = 'tests/fixtures/file1.yml'
    pathfile2 = 'tests/fixtures/file2.yml'
    with open(pathfile1, 'r'):
        with open(pathfile2, 'r'):
            with open('tests/fixtures/result_yml', 'r') as result:
                result = result.read()
                assert generate_diff(pathfile1, pathfile2) == result


def test_parser_json():
    result = {'host': 'hexlet.io',
              'timeout': 50,
              'proxy': '123.234.53.22',
              'follow': False,
              }
    pathfile = 'tests/fixtures/file1.json'
    assert parser(pathfile) == result


def test_parser_path():
    pathfile = 'tests/fixtures/bad.path'
    with pytest.raises(ValueError, match=f"{pathfile} doesn't exists"):
        parser(pathfile)


def test_parser_extension():
    pathfile = 'tests/fixtures/file1.bad_ext'
    with pytest.raises(ValueError, match='enexpected extension of the file: file1.bad_ext'):
        parser(pathfile)
