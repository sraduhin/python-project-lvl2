from gendiff.comparer import run_differ
from gendiff.parser.parser import parser
from gendiff.printer import show_diff
import pytest

plain = {
    '- follow': False,
    '  host': 'hexlet.io',
    '- proxy': '123.234.53.22',
    '- timeout': 50,
    '+ timeout': 20,
    '+ verbose': True,
}

nested = {
    '  common': {
        '+ follow': False,
        '  setting1': 'Value 1',
        '- setting2': 200,
        '- setting3': True,
        '+ setting3': None,
        '+ setting4': 'blah blah',
        '+ setting5': {
            '  key5': 'value5',
        },
        '  setting6': {
            '  doge': {
                '- wow': '',
                '+ wow': 'so much',
            },
            '  key': 'value',
            '+ ops': 'vops',
        },
    },
    '  group1': {
        '- baz': 'bas',
        '+ baz': 'bars',
        '  foo': 'bar',
        '- nest': {
            '  key': 'value',
        },
        '+ nest': 'str',
    },
    '- group2': {
        '  abc': 12345,
        '  deep': {
            '  id': 45,
        },
    },
    '+ group3': {
        '  deep': {
            '  id': {
                '  number': 45,
            },
        },
        '  fee': 100500,
    },
}


def test_generate_diff_plain_json():
    pathfile1 = 'tests/fixtures/plain/file1.json'
    pathfile2 = 'tests/fixtures/plain/file2.json'
    with open(pathfile1, 'r'):
        with open(pathfile2, 'r'):
            result = plain
            assert run_differ(pathfile1, pathfile2) == result


def test_generate_diff_nested_json():
    pathfile1 = 'tests/fixtures/nested/file1.json'
    pathfile2 = 'tests/fixtures/nested/file2.json'
    with open(pathfile1, 'r'):
        with open(pathfile2, 'r'):
            result = nested
            print(result)
            print(run_differ(pathfile1, pathfile2))
            assert run_differ(pathfile1, pathfile2) == result


def test_generate_diff_plain_yml():
    pathfile1 = 'tests/fixtures/plain/file1.yml'
    pathfile2 = 'tests/fixtures/plain/file2.yml'
    with open(pathfile1, 'r'):
        with open(pathfile2, 'r'):
            result = plain
            assert run_differ(pathfile1, pathfile2) == result


def test_parser_path():
    pathfile = 'tests/fixtures/bad.path'
    with pytest.raises(ValueError, match=f"{pathfile} doesn't exists"):
        parser(pathfile)


def test_parser_extension():
    pathfile = 'tests/fixtures/plain/file1.bad_ext'
    with pytest.raises(ValueError, match='enexpected extension of the file: file1.bad_ext'):
        parser(pathfile)


def test_show_diff_plain():
    pathfile = 'tests/fixtures/plain/result'
    with open(pathfile, 'r') as f:
        result = f.read()
        assert show_diff(plain) == result


def test_show_diff_nested():
    pathfile = 'tests/fixtures/nested/result'
    with open(pathfile, 'r') as f:
        result = f.read()
        print('result')
        print(result)
        print('SD')
        print(show_diff(nested))
        assert show_diff(nested) == result
