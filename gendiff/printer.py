def print_diff(data, replacer = '  '):
    def go_deeper(data, depth):
        result = ''
        if not isinstance(data, list):
            result += f'{data or ""}'
        else:
            depth += 2
            result += '{\n'
            for item in data:
                result += f'{replacer * depth}{item["operator"] or " "} {item["name"]}: {go_deeper(item["value"], depth)}\n'
            result += f'{replacer * (depth - 1)}'
            result += '}'
        return result
    print (go_deeper(data, 0))

data = [
    {
        'name': "common",
        'operator': None,
        'value': [
            {
                'name': "follow",
                'operator': "+",
                'value': "false"
            },
            {
                'name': "setting2",
                'operator': "-",
                'value': "200"
            },
            {
                'name': "setting3",
                'operator': "-",
                'value': "true"
            },
            {
                'name': "setting3",
                'operator': "+",
                'value': "null"
            },
            {
                'name': "setting4",
                'operator': "+",
                'value': "blah blah"
            },
            {
                'name': "setting5",
                'operator': "+",
                'value': [
                    {
                        'name': "key5",
                        'operator': None,
                        'value': "value5"
                    }
                ]
            },
            {
                'name': "setting6",
                'operator': None,
                'value': [
                    {
                        'name': "doge",
                        'operator': None,
                        'value': [
                            {
                                'name': "wow",
                                'operator': "-",
                                'value': None
                            },
                            {
                                'name': "wow",
                                'operator': "+",
                                'value': "so much"
                            }
                        ]
                    },
                    {
                        'name': "key",
                        'operator': None,
                        'value': "value"
                    },
                    {
                        'name': "ops",
                        'operator': "+",
                        'value': "vops"
                    }
                ]
            }
        ]
    },
    {
        'name': "group1",
        'operator': None,
        'value': [
            {
                'name': "baz",
                'operator': "-",
                'value': "bas"
            },
            {
                'name': "baz",
                'operator': "+",
                'value': "bars"
            },
            {
                'name': "foo",
                'operator': None,
                'value': "bar"
            },
            {
                'name': "nest",
                'operator': "-",
                'value': [
                    {
                        'name': "key",
                        'operator': None,
                        'value': "value"
                    }
                ]
            },
            {
                'name': "nest",
                'operator': "+",
                'value': "str"
            }
        ]
    },
    {
        'name': "group2",
        'operator': "-",
        'value': [
            {
                'name': "abc",
                'operator': None,
                'value': "12345"
            },
            {
                'name': "deep",
                'operator': None,
                'value': [
                    {
                        'name': "id",
                        'operator': None,
                        'value': "45"
                    }
                ]
            }
        ]
    },
    {
        'name': "group3",
        'operator': "+",
        'value': [
            {
                'name': "deep",
                'operator': None,
                'value': [
                    {
                        'name': "id",
                        'operator': None,
                        'value': [
                            {
                                'name': "number",
                                'operator': None,
                                'value': "45"
                            }
                        ]
                    }
                ]
            },
            {
                'name': "fee",
                'operator': None,
                'value': "100500"
            }
        ]
    }
]


if __name__ == "__main__":
    print_diff(data)