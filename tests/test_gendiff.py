from gendiff.comparer import generate_diff
from gendiff.printer import print_diff
from gendiff.parser.parser import parser
import pytest



def test_generate_diff_json():
    pathfile1 = 'tests/fixtures/plain/file1.json'
    pathfile2 = 'tests/fixtures/plain/file2.json'
    with open(pathfile1, 'r'):
        with open(pathfile2, 'r'):
            with open('tests/fixtures/plain/result_printed', 'r') as result:
                result = result.read()
                assert generate_diff(pathfile1, pathfile2) == result


def test_generate_diff_yml():
    pathfile1 = 'tests/fixtures/plain/file1.yml'
    pathfile2 = 'tests/fixtures/plain/file2.yml'
    with open(pathfile1, 'r'):
        with open(pathfile2, 'r'):
            with open('tests/fixtures/plain/result_printed', 'r') as result:
                result = result.read()
                assert generate_diff(pathfile1, pathfile2) == result


def test_parser_json():
    result = {'host': 'hexlet.io',
              'timeout': 50,
              'proxy': '123.234.53.22',
              'follow': False,
              }
    pathfile = 'tests/fixtures/plain/file1.json'
    assert parser(pathfile) == result


def test_parser_path():
    pathfile = 'tests/fixtures/bad.path'
    with pytest.raises(ValueError, match=f"{pathfile} doesn't exists"):
        parser(pathfile)


def test_parser_extension():
    pathfile = 'tests/fixtures/plain/file1.bad_ext'
    with pytest.raises(ValueError, match='enexpected extension of the file: file1.bad_ext'):
        parser(pathfile)

def test_printer():
    data = [
    {
        'name': "common",
        'operator': None,
        'value': [
            {
                'name': "follow",
                'operator': "+",
                'value': "false"
            },
            {
                'name': "setting1",
                'operator': None,
                'value': "Value 1"
            },
            {
                'name': "setting2",
                'operator': "-",
                'value': "200"
            },
            {
                'name': "setting3",
                'operator': "-",
                'value': "true"
            },
            {
                'name': "setting3",
                'operator': "+",
                'value': "null"
            },
            {
                'name': "setting4",
                'operator': "+",
                'value': "blah blah"
            },
            {
                'name': "setting5",
                'operator': "+",
                'value': [
                    {
                        'name': "key5",
                        'operator': None,
                        'value': "value5"
                    }
                ]
            },
            {
                'name': "setting6",
                'operator': None,
                'value': [
                    {
                        'name': "doge",
                        'operator': None,
                        'value': [
                            {
                                'name': "wow",
                                'operator': "-",
                                'value': None
                            },
                            {
                                'name': "wow",
                                'operator': "+",
                                'value': "so much"
                            }
                        ]
                    },
                    {
                        'name': "key",
                        'operator': None,
                        'value': "value"
                    },
                    {
                        'name': "ops",
                        'operator': "+",
                        'value': "vops"
                    }
                ]
            }
        ]
    },
    {
        'name': "group1",
        'operator': None,
        'value': [
            {
                'name': "baz",
                'operator': "-",
                'value': "bas"
            },
            {
                'name': "baz",
                'operator': "+",
                'value': "bars"
            },
            {
                'name': "foo",
                'operator': None,
                'value': "bar"
            },
            {
                'name': "nest",
                'operator': "-",
                'value': [
                    {
                        'name': "key",
                        'operator': None,
                        'value': "value"
                    }
                ]
            },
            {
                'name': "nest",
                'operator': "+",
                'value': "str"
            }
        ]
    },
    {
        'name': "group2",
        'operator': "-",
        'value': [
            {
                'name': "abc",
                'operator': None,
                'value': "12345"
            },
            {
                'name': "deep",
                'operator': None,
                'value': [
                    {
                        'name': "id",
                        'operator': None,
                        'value': "45"
                    }
                ]
            }
        ]
    },
    {
        'name': "group3",
        'operator': "+",
        'value': [
            {
                'name': "deep",
                'operator': None,
                'value': [
                    {
                        'name': "id",
                        'operator': None,
                        'value': [
                            {
                                'name': "number",
                                'operator': None,
                                'value': "45"
                            }
                        ]
                    }
                ]
            },
            {
                'name': "fee",
                'operator': None,
                'value': "100500"
            }
        ]
    }
]
    with open('tests/fixtures/nested/result_printed', 'r') as result:
        result = result.read()
        print('>>>print_diff(data)')
        print(print_diff(data))
        print('>>>result')
        print(result)
        assert print_diff(data) == result