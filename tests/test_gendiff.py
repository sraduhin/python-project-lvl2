from gendiff.comparer import compare
from gendiff.parser.parser import parse_file, load_file
from gendiff.formatter.stylish import stylish_formatter
from gendiff.formatter.plain import plain_formatter
from gendiff.formatter.json import json_formatter
import pytest
import tests.expected_data as expected


def get_path(endpath):
    return 'tests/fixtures/' + endpath


def test_parser_path():
    '''test wrong pathfile'''
    pathfile = get_path('bad.path')
    with pytest.raises(ValueError, match=f"{pathfile} doesn't exists"):
        load_file(pathfile)


def test_parser_extension():
    '''test wrong extension'''
    pathfile = get_path('simple/file1.bad_ext')
    with pytest.raises(ValueError,
                       match='enexpected extension of the file: file1.bad_ext'):
        load_file(pathfile)


def test_parser_simple_json():
    '''test parse simple json'''
    pathfile = get_path('simple/file1.json')
    data = expected.SIMPLE_PARSED_DATA
    content, extension = load_file(pathfile)
    assert parse_file(content, extension) == data
    assert parse_file(content) == data


def test_parser_nested_json():
    '''test parse complex json'''
    pathfile = get_path('nested/file1.json')
    data = expected.NESTED_PARSED_DATA
    content, extension = load_file(pathfile)
    assert parse_file(content, extension) == data
    assert parse_file(content) == data


def test_parser_simple_yml():
    '''test parse simple yaml'''
    pathfile = get_path('simple/file1.yml')
    data = expected.SIMPLE_PARSED_DATA
    content, extension = load_file(pathfile)
    assert parse_file(content, extension) == data
    assert parse_file(content) == data


def test_parser_nested_yml():
    '''test parse complex yaml'''
    pathfile = get_path('nested/file1.yaml')
    data = expected.NESTED_PARSED_DATA
    content, extension = load_file(pathfile)
    assert parse_file(content, extension) == data
    assert parse_file(content) == data


def test_generate_diff_simple():
    '''test compare simple json'''
    data1, _ = load_file('tests/fixtures/simple/file1.json')
    data2, _ = load_file('tests/fixtures/simple/file2.json')
    assert compare(parse_file(data1), parse_file(data2)) == expected.SIMPLE_REPR


def test_generate_diff_nested():
    '''test compare complex json'''
    data1, _ = load_file('tests/fixtures/nested/file1.json')
    data2, _ = load_file('tests/fixtures/nested/file2.json')
    assert compare(parse_file(data1), parse_file(data2)) == expected.NESTED_REPR


def test_show_diff():
    '''test all formatters types'''
    assert stylish_formatter(expected.SIMPLE_REPR) == expected.SIMPLE_DATA_RESULT_STYLISH  # noqa:E501
    assert stylish_formatter(expected.NESTED_REPR) == expected.NESTED_DATA_RESULT_STYLISH  # noqa:E501
    assert plain_formatter(expected.SIMPLE_REPR) == expected.SIMPLE_DATA_RESULT_PLAIN  # noqa:E501
    assert plain_formatter(expected.NESTED_REPR) == expected.NESTED_DATA_RESULT_PLAIN  # noqa:E501
    assert json_formatter(expected.SIMPLE_REPR) == expected.SIMPLE_DATA_RESULT_JSON  # noqa:E501
    assert json_formatter(expected.NESTED_REPR) == expected.NESTED_DATA_RESULT_JSON  # noqa:E501
