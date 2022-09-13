from gendiff.comparer import generate_diff
from gendiff.parser.parser import parser
from gendiff.formatter.stylish import main as show_diff_stylish
from gendiff.formatter.plain import main as show_diff_plain
import pytest
import tests.expected_data as expected


def test_parser_path():
    pathfile = 'tests/fixtures/bad.path'
    with pytest.raises(ValueError, match=f"{pathfile} doesn't exists"):
        parser(pathfile)


def test_parser_extension():
    pathfile = 'tests/fixtures/simple/file1.bad_ext'
    with pytest.raises(ValueError, match='enexpected extension of the file: file1.bad_ext'):
        parser(pathfile)


def test_parser_simple_json():
    pathfile = 'tests/fixtures/simple/file1.json'
    data = expected.SIMPLE_PARSED_DATA
    assert parser(pathfile) == data


def test_parser_nested_json():
    pathfile = 'tests/fixtures/nested/file1.json'
    data = expected.NESTED_PARSED_DATA
    assert parser(pathfile) == data


def test_parser_simple_yml():
    pathfile = 'tests/fixtures/simple/file1.yml'
    data = expected.SIMPLE_PARSED_DATA
    assert parser(pathfile) == data


def test_parser_nested_yml():
    pathfile = 'tests/fixtures/nested/file1.yaml'
    data = expected.NESTED_PARSED_DATA
    assert parser(pathfile) == data


def test_generate_diff_simple():
    data1 = parser('tests/fixtures/simple/file1.json')
    data2 = parser('tests/fixtures/simple/file2.json')
    assert generate_diff(data1, data2) == expected.SIMPLE_REPR


def test_generate_diff_nested():
    data1 = parser('tests/fixtures/nested/file1.json')
    data2 = parser('tests/fixtures/nested/file2.json')
    assert generate_diff(data1, data2) == expected.NESTED_REPR


def test_show_diff_simple_stylish():
    pathfile = 'tests/fixtures/simple/result_stylish'
    with open(pathfile, 'r') as f:
        result = f.read()
        assert show_diff_stylish(SIMPLE_RESULT) == result


def test_show_diff_nested_stylish():
    pathfile = 'tests/fixtures/nested/result_stylish'
    with open(pathfile, 'r') as f:
        result = f.read()
        assert show_diff_stylish(NESTED_RESULT) == result


def test_show_diff_simple_plain():
    pathfile = 'tests/fixtures/simple/result_plain'
    with open(pathfile, 'r') as f:
        result = f.read()
        assert show_diff_plain(SIMPLE_RESULT) == result


def test_show_diff_nested_plain():
    pathfile = 'tests/fixtures/nested/result_plain'
    with open(pathfile, 'r') as f:
        result = f.read()
        assert show_diff_plain(NESTED_RESULT) == result
