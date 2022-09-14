from gendiff.comparer import compare
from gendiff.parser.parser import parser
from gendiff.formatter.stylish import main as show_diff_stylish
from gendiff.formatter.plain import main as show_diff_plain
from gendiff.formatter.plain import main as show_diff_json
import pytest
import tests.expected_data as expected


def get_path(endpath):
    return 'tests/fixtures/' + endpath


def test_parser_path():
    pathfile = get_path('bad.path')
    with pytest.raises(ValueError, match=f"{pathfile} doesn't exists"):
        parser(pathfile)


def test_parser_extension():
    pathfile = get_path('simple/file1.bad_ext')
    with pytest.raises(ValueError, match='enexpected extension of the file: file1.bad_ext'):
        parser(pathfile)


def test_parser_simple_json():
    pathfile = get_path('simple/file1.json')
    data = expected.SIMPLE_PARSED_DATA
    assert parser(pathfile) == data


def test_parser_nested_json():
    pathfile = get_path('nested/file1.json')
    data = expected.NESTED_PARSED_DATA
    assert parser(pathfile) == data


def test_parser_simple_yml():
    pathfile = get_path('simple/file1.yml')
    data = expected.SIMPLE_PARSED_DATA
    assert parser(pathfile) == data


def test_parser_nested_yml():
    pathfile = get_path('nested/file1.yaml')
    data = expected.NESTED_PARSED_DATA
    assert parser(pathfile) == data


def test_generate_diff_simple():
    data1 = parser('tests/fixtures/simple/file1.json')
    data2 = parser('tests/fixtures/simple/file2.json')
    assert compare(data1, data2) == expected.SIMPLE_REPR


def test_generate_diff_nested():
    data1 = parser('tests/fixtures/nested/file1.json')
    data2 = parser('tests/fixtures/nested/file2.json')
    assert compare(data1, data2) == expected.NESTED_REPR


def test_show_diff():
    assert show_diff_stylish(expected.SIMPLE_REPR) == expected.SIMPLE_DATA_RESULT_STYLISH
    assert show_diff_stylish(expected.NESTED_REPR) == expected.NESTED_DATA_RESULT_STYLISH
    assert show_diff_plain(expected.SIMPLE_REPR) == expected.SIMPLE_DATA_RESULT_PLAIN
    assert show_diff_plain(expected.NESTED_REPR) == expected.NESTED_DATA_RESULT_PLAIN
    assert show_diff_json(expected.SIMPLE_REPR) == expected.SIMPLE_DATA_RESULT_PLAIN
    assert show_diff_json(expected.NESTED_REPR) == expected.NESTED_DATA_RESULT_PLAIN
