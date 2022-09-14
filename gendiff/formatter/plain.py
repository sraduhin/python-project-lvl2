def normalize(data):
    if isinstance(data, bool):
        return f'{data}'.lower()
    if isinstance(data, int):
        return data
    if data is None:
        return 'null'
    return '[complex value]' if isinstance(data, dict) else f"'{data}'"


def main(data):
    def inner(data, depth=[]):
        result = ''
        for key, value in data.items():
            if not isinstance(value, dict):
                continue
            depth.append(key)
            if isinstance(value, dict) and value.get('action'):
                action = value['action']
                result += f"Property '{'.'.join(depth)}' was "
                if action == '+':
                    result += f"added with value: {normalize(value['value'])}\n"
                elif action == '-':
                    result += 'removed\n'
                else:
                    result += f"updated. From {normalize(value['old_value'])} "
                    result += f"to {normalize(value['new_value'])}\n"
            else:
                result += inner(value, depth)
            depth.pop()
        return result
    return inner(data)[:-1]


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
    print('>>>')
    print(main(NESTED_REPR))
