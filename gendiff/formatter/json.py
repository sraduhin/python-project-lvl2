import json


def main(data):
    return json.dumps(data, indent=4)


if __name__ == "__main__":
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

    print(main(SIMPLE_REPR))
    print(main(SIMPLE_REPR))
