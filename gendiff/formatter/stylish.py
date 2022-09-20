# stylish formattef
import json
import re

TYPES = ['added', 'removed', 'updated', 'no changes']


def get_type(type):
    return {
        'added': '+',
        'no changes': ' ',
        'removed': '-'
    }[type]


def make_tree(data):
    '''
    function rebuild dictionary representation
    '''
    result = {}
    if not isinstance(data, dict):
        return data
    for key, value in data.items():
        if not isinstance(value, dict):
            result[f'  {key}'] = value
        elif not data[key].get('type') in TYPES:
            result[f'  {key}'] = make_tree(value)
        else:
            type = data[key].get('type')
            if type == 'updated':
                result[f'- {key}'] = make_tree(value['old_value'])
                result[f'+ {key}'] = make_tree(value['new_value'])
            else:
                print('check value', value)
                result[f'{get_type(type)} {key}'] = make_tree(value['value'])
    return result


def stringify(data):
    '''
    function cuts \' and fixes indents
    '''
    result = json.dumps(data, indent=4)
    result = result.replace('"', '')
    result = result.replace(',', '')
    result = result.replace('  }', '    }')
    result = re.sub(r"\n\s\s", '\n', result)
    return result


def stylish_formatter(data):
    result = make_tree(data)
    return stringify(result)

if __name__ == "__main__":
    d = {
    'common': {
        'follow': {
            'type': 'added', 
            'value': False
        }, 'setting1': {
            'type': 'no changes', 
            'value': 'Value 1'
        }, 'setting2': {
            'type': 'removed', 
            'value': 200
        }, 
        'setting3': {
            'type': 'updated', 
            'old_value': True, 
            'new_value': {
                'key': 'value'
            }
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
            'doge': {
                'wow': {
                    'type': 'updated', 
                    'old_value': 'too much', 
                    'new_value': 'so much'
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
    }, 
    'group1': {
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
    }, 
    'group4': {
        'default': {
            'type': 'updated', 
            'old_value': None, 
            'new_value': ''
        }, 
        'foo': {
            'type': 'updated', 
            'old_value': 0, 
            'new_value': None
        }, 
        'isNested': {
            'type': 'updated', 
            'old_value': False, 
            'new_value': 'none'
        }, 
        'key': {
            'type': 'added', 
            'value': False
        }, 
        'nest': {
            'bar': {
                'type': 'updated', 
                'old_value': '', 
                'new_value': 0
            }, 
            'isNested': {
                'type': 'removed', 
                'value': True
            }
        }, 
        'someKey': {
            'type': 'added', 
            'value': True
        }, 
        'type': {
            'type': 'updated', 
            'old_value': 'bas', 
            'new_value': 'bar'
        }
    }
}
    print(make_tree(d))
