from gendiff.comparer import generate_diff
from gendiff.parser.parser import parser
from gendiff.formatter.stylish import main as show_diff_stylish
from gendiff.formatter.plain import main as show_diff_plain
import pytest

@pytest.fixture
def build_result():
    SIMPLE_RESULT = [
        ('follow', 'remove', False),
        ('host', None, 'hexlet.io'),
        ('proxy', 'remove', '123.234.53.22'),
        ('timeout', 'update', (50, 20)),
        ('verbose', 'add', True)
        ]
    NESTED_RESULT = [
        ('common', None,[
            ('follow', 'add', False),
            ('setting1', None, 'Value 1'),
            ('setting2', 'remove', 200),
            ('setting3', 'update', (True, None)),
            ('setting4', 'add', 'blah blah'),
            ('setting5', 'add', [
                ('key5', None, 'value5')
                ]),
            ('setting6', None, [
                ('doge', None, [
                    ('wow', 'update', ('', 'so much'))
                ]),
                ('key', None, 'value'),
                ('ops', 'add', 'vops')
            ])]),
        ('group1', None, [
            ('baz', 'update', ('bas', 'bars')),
            ('foo', None, 'bar'),
            ('nest', 'update', ([
                ('key', None, 'value')
            ], 'str'))
        ]),
        ('group2', 'remove', [
            ('abc', None, 12345),
            ('deep', None, [
                ('id', None, 45)
            ])]),
        ('group3', 'add', [
            ('deep', None, [
                ('id', None, [
                    ('number', None, 45)
                ])
            ]),
            ('fee', None, 100500)
        ])
    ]
    return (SIMPLE_RESULT, NESTED_RESULT)


@pytest.fixture
def parse_result():
    SIMPLE_RESULT = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }
    NESTED_RESULT = {
        'common': {
            'setting1': 'Value 1',
            'setting2': 200,
            'setting3': True,
            'setting6': {
                'key': 'value',
                'doge': {
                    'wow': ''
                }
            }
        },
        'group1': {
            'baz': 'bas',
            'foo': 'bar',
            'nest': {
                'key': 'value'
            }
        },
        'group2': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        }
    }
    return (SIMPLE_RESULT, NESTED_RESULT)


NESTED_RESULT = [('common', None, [('follow', 'add', False), ('setting1', None, 'Value 1'), ('setting2', 'remove', 200), ('setting3', 'update', (True, None)), ('setting4', 'add', 'blah blah'), ('setting5', 'add', [('key5', None, 'value5')]), ('setting6', None, [('doge', None, [('wow', 'update', ('', 'so much'))]), ('key', None, 'value'), ('ops', 'add', 'vops')])]), ('group1', None, [('baz', 'update', ('bas', 'bars')), ('foo', None, 'bar'), ('nest', 'update', ([('key', None, 'value')], 'str'))]), ('group2', 'remove', [('abc', None, 12345), ('deep', None, [('id', None, 45)])]), ('group3', 'add', [('deep', None, [('id', None, [('number', None, 45)])]), ('fee', None, 100500)])]

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
    data = parse_result[0]
    assert parser(pathfile) == data


def test_parser_nested_json():
    pathfile = 'tests/fixtures/nested/file1.json'
    data = parse_result[1]
    assert parser(pathfile) == data


def test_parser_simple_yml():
    pathfile = 'tests/fixtures/simple/file1.yml'
    data = parse_result[0]
    assert parser(pathfile) == data


def test_parser_nested_yml():
    pathfile = 'tests/fixtures/nested/file1.yaml'
    data = parse_result[1]
    assert parser(pathfile) == data


def test_generate_diff_simple():
    data1 = parser('tests/fixtures/simple/file1.json')
    data2 = parser('tests/fixtures/simple/file2.json')
    assert generate_diff(data1, data2) == build_result[0]


def test_generate_diff_nested():
    data1 = parser('tests/fixtures/nested/file1.json')
    data2 = parser('tests/fixtures/nested/file2.json')
    assert generate_diff(data1, data2) == build_result[1]


def test_show_diff_simple_stylish():
    pathfile = 'tests/fixtures/simple/result_stylish'
    with open(pathfile, 'r') as f:
        result = show_diff_stylish(build_result[0])
        assert result == f.read()


def test_show_diff_nested_stylish():
    pathfile = 'tests/fixtures/nested/result_stylish'
    with open(pathfile, 'r') as f:
        result = show_diff_stylish(build_result[1])
        assert result == f.read()


def test_show_diff_simple_plain():
    pathfile = 'tests/fixtures/simple/result_plain'
    with open(pathfile, 'r') as f:
        result = show_diff_plain(build_result[0])
        assert result == f.read()


def test_show_diff_nested_plain():
    pathfile = 'tests/fixtures/nested/result_plain'
    with open(pathfile, 'r') as f:
        result = show_diff_plain(build_result[1])
        assert result == f.read()
