from gendiff.comparer import generate_diff
from gendiff.parser.parser import parser
from gendiff.printer import show_diff_stylish
import pytest


SIMPLE_RESULT = {'follow': {'action': 'removed', 'value': False}, 'host': {'value': 'hexlet.io'}, 'proxy': {'action': 'removed', 'value': '123.234.53.22'}, 'timeout': {'action': 'updated', 'From': 50, 'to': 20}, 'verbose': {'action': 'added', 'value': True}}

NESTED_RESULT = {'common': {'follow': {'action': 'added', 'value': False}, 'setting1': {'value': 'Value 1'}, 'setting2': {'action': 'removed', 'value': 200}, 'setting3': {'action': 'updated', 'From': True, 'to': None}, 'setting4': {'action': 'added', 'value': 'blah blah'}, 'setting5': {'action': 'added', 'value': {'key5': 'value5'}}, 'setting6': {'doge': {'wow': {'action': 'updated', 'From': '', 'to': 'so much'}}, 'key': {'value': 'value'}, 'ops': {'action': 'added', 'value': 'vops'}}}, 'group1': {'baz': {'action': 'updated', 'From': 'bas', 'to': 'bars'}, 'foo': {'value': 'bar'}, 'nest': {'action': 'updated', 'From': {'key': 'value'}, 'to': 'str'}}, 'group2': {'action': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}}, 'group3': {'action': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}


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
    data = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    assert parser(pathfile) == data


def test_parser_nested_json():
    pathfile = 'tests/fixtures/nested/file1.json'
    data = {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': ''}}}, 'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}}, 'group2': {'abc': 12345, 'deep': {'id': 45}}}
    assert parser(pathfile) == data


def test_parser_simple_yml():
    pathfile = 'tests/fixtures/simple/file1.yml'
    data = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
    assert parser(pathfile) == data


def test_parser_nested_yml():
    pathfile = 'tests/fixtures/nested/file1.yaml'
    data = {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': ''}}}, 'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}}, 'group2': {'abc': 12345, 'deep': {'id': 45}}}
    assert parser(pathfile) == data


def test_generate_diff_simple():
    data1 = parser('tests/fixtures/simple/file1.json')
    data2 = parser('tests/fixtures/simple/file2.json')
    assert generate_diff(data1, data2) == SIMPLE_RESULT


def test_generate_diff_nested():
    data1 = parser('tests/fixtures/nested/file1.json')
    data2 = parser('tests/fixtures/nested/file2.json')
    assert generate_diff(data1, data2) == NESTED_RESULT


def test_show_diff_simple():
    pathfile = 'tests/fixtures/simple/result'
    with open(pathfile, 'r') as f:
        result = f.read()
        print(result)
        print('>>>')
        print(show_diff_stylish(SIMPLE_RESULT))
        assert show_diff_stylish(SIMPLE_RESULT) == result


def test_show_diff_nested():
    pathfile = 'tests/fixtures/nested/result'
    with open(pathfile, 'r') as f:
        result = f.read()
        assert show_diff_stylish(NESTED_RESULT) == result
