SIMPLE_REPR = {
    'follow': {
        'action': '-', 'value': False
    },
    'host': 'hexlet.io',
    'proxy': {
        'action': '-',
        'value': '123.234.53.22'
    },
    'timeout': {
        'action': 'update',
        'old_value': 50,
        'new_value': 20
    },
    'verbose': {
        'action': '+',
        'value': True
    }
}

NESTED_REPR = {
    'common': {
        'follow': {
            'action': '+',
            'value': False
        },
        'setting1': 'Value 1',
        'setting2': {
            'action': '-',
            'value': 200
        },
        'setting3': {
            'action': 'update',
            'old_value': True,
            'new_value': None
        },
        'setting4': {
            'action': '+',
            'value': 'blah blah'
        },
        'setting5': {
            'action': '+',
            'value': {
                'key5': 'value5'
            }
        },
        'setting6': {
            'doge': {
                'wow': {
                    'action': 'update',
                    'old_value': '',
                    'new_value': 'so much'
                }
            },
            'key': 'value',
            'ops': {
                'action': '+',
                'value': 'vops'
            }
        }
    },
    'group1': {
        'baz': {
            'action': 'update',
            'old_value': 'bas',
            'new_value': 'bars'
        },
        'foo': 'bar',
        'nest': {
            'action': 'update',
            'old_value': {
                'key': 'value'
            },
            'new_value': 'str'
        }
    },
    'group2': {
        'action': '-',
        'value': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        }
    },
    'group3': {
        'action': '+',
        'value': {
            'deep': {
                'id': {
                    'number': 45
                }
            },
            'fee': 100500
        }
    }
}

SIMPLE_PARSED_DATA = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False
}

NESTED_PARSED_DATA = {
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

with open('tests/fixtures/result/plain', r) as f:
    SIMPLE_DATA_RESULT_PLAIN, NESTED_DATA_RESULT_PLAIN = f.read().split('\n\n')

with open('tests/fixtures/result/plain', r) as f:
    SIMPLE_DATA_RESULT_STYLISH, NESTED_DATA_RESULT_STYLISH = f.read().split('\n\n')
    
with open('tests/fixtures/result/plain', r) as f:
    SIMPLE_DATA_RESULT_JSON, NESTED_DATA_RESULT_JSON = f.read().split('\n\n')
