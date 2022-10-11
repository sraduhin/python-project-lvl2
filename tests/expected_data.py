SIMPLE_REPR = {
    'follow': {
        'type': 'removed',
        'value': False
    },
    'host': {
        'type': 'no changes',
        'value': 'hexlet.io'
    },
    'proxy': {
        'type': 'removed',
        'value': '123.234.53.22'
    },
    'timeout': {
        'type': 'updated',
        'old_value': 50,
        'new_value': 20
    },
    'verbose': {
        'type': 'added',
        'value': True
    }
}

NESTED_REPR = {
    'common': {
        'type': 'children',
        'value': {
            'follow': {
                'type': 'added',
                'value': False
            },
            'setting1': {
                'type': 'no changes',
                'value': 'Value 1'
            },
            'setting2': {
                'type': 'removed',
                'value': 200
            },
            'setting3': {
                'type': 'updated',
                'old_value': True,
                'new_value': None
            },
            'setting4': {
                'type': 'added',
                'value': 'blah blah'
            },
            'setting5': {
                'type': 'added',
                'value': {
                    'key5': 'value5'
                }
            },
            'setting6': {
                'type': 'children',
                'value': {
                    'doge': {
                        'type': 'children',
                        'value': {
                            'wow': {
                                'type': 'updated',
                                'old_value': '',
                                'new_value': 'so much'
                            }
                        }
                    },
                    'key': {
                        'type': 'no changes',
                        'value': 'value'
                    },
                    'ops': {
                        'type': 'added',
                        'value': 'vops'
                    }
                }
            }
        }
    },
    'group1': {
        'type': 'children',
        'value': {
            'baz': {
                'type': 'updated',
                'old_value': 'bas',
                'new_value': 'bars'
            },
            'foo': {
                'type': 'no changes',
                'value': 'bar'
            },
            'nest': {
                'type': 'updated',
                'old_value': {
                    'key': 'value'
                },
                'new_value': 'str'
            }
        }
    },
    'group2': {
        'type': 'removed',
        'value': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        }
    },
    'group3': {
        'type': 'added',
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

with open('tests/fixtures/result/plain', 'r') as f:
    SIMPLE_DATA_RESULT_PLAIN, NESTED_DATA_RESULT_PLAIN = f.read().split('\n\n')

with open('tests/fixtures/result/stylish', 'r') as f:
    SIMPLE_DATA_RESULT_STYLISH, NESTED_DATA_RESULT_STYLISH = f.read().split('\n\n') # noqa E501

with open('tests/fixtures/result/json', 'r') as f:
    SIMPLE_DATA_RESULT_JSON, NESTED_DATA_RESULT_JSON = f.read().split('\n\n')
