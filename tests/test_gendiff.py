from gendiff.comparer import run_differ
from gendiff.parser.parser import parser
from gendiff.printer import show_diff
import pytest

plain = {'follow': {'value': False, 'operator': '-'}, 'host': {'value': 'hexlet.io'}, 'proxy': {'value': '123.234.53.22', 'operator': '-'}, 'timeout': {'value': 20, 'operator': '+'}, 'verbose': {'value': True, 'operator': '+'}}

nested = {'common': {'value': {'follow': {'value': False, 'operator': '+'}, 'setting1': {'value': 'Value 1'}, 'setting2': {'value': 200, 'operator': '-'}, 'setting3': {'value': None, 'operator': '+'}, 'setting4': {'value': 'blah blah', 'operator': '+'}, 'setting5': {'value': {'key5': {'value': 'value5'}}, 'operator': '+'}, 'setting6': {'value': {'doge': {'value': {'wow': {'value': 'so much', 'operator': '+'}}}, 'key': {'value': 'value'}, 'ops': {'value': 'vops', 'operator': '+'}}}}}, 'group1': {'value': {'baz': {'value': 'bars', 'operator': '+'}, 'foo': {'value': 'bar'}, 'nest': {'value': 'str', 'operator': '+'}}}, 'group2': {'value': {'abc': {'value': 12345}, 'deep': {'value': {'id': {'value': 45}}}}, 'operator': '-'}, 'group3': {'value': {'deep': {'value': {'id': {'value': {'number': {'value': 45}}}}}, 'fee': {'value': 100500}}, 'operator': '+'}}


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
