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

SIMPLE_DATA_RESULT_PLAIN = '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true'''

SIMPLE_DATA_RESULT_STYLISH = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

SIMPLE_DATA_RESULT_JSON = '''{
    "follow": {
        "action": "-",
        "value": false
    },
    "host": "hexlet.io",
    "proxy": {
        "action": "-",
        "value": "123.234.53.22"
    },
    "timeout": {
        "action": "update",
        "old_value": 50,
        "new_value": 20
    },
    "verbose": {
        "action": "+",
        "value": true
    }
}'''

NESTED_DATA_RESULT_PLAIN = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

NESTED_DATA_RESULT_STYLISH = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

NESTED_DATA_RESULT_JSON = '''{
    "common": {
        "follow": {
            "action": "+",
            "value": false
        },
        "setting1": "Value 1",
        "setting2": {
            "action": "-",
            "value": 200
        },
        "setting3": {
            "action": "update",
            "old_value": true,
            "new_value": null
        },
        "setting4": {
            "action": "+",
            "value": "blah blah"
        },
        "setting5": {
            "action": "+",
            "value": {
                "key5": "value5"
            }
        },
        "setting6": {
            "doge": {
                "wow": {
                    "action": "update",
                    "old_value": "",
                    "new_value": "so much"
                }
            },
            "key": "value",
            "ops": {
                "action": "+",
                "value": "vops"
            }
        }
    },
    "group1": {
        "baz": {
            "action": "update",
            "old_value": "bas",
            "new_value": "bars"
        },
        "foo": "bar",
        "nest": {
            "action": "update",
            "old_value": {
                "key": "value"
            },
            "new_value": "str"
        }
    },
    "group2": {
        "action": "-",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    "group3": {
        "action": "+",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
}'''
