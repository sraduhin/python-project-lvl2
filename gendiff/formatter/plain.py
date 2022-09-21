# plain formatter


def normalize(data):
    '''
    funcion convert bool to str, nested to "[complex value]"
    '''
    if isinstance(data, bool):
        return f'{data}'.lower()
    if isinstance(data, int):
        return data
    if data is None:
        return 'null'
    return '[complex value]' if isinstance(data, dict) else f"'{data}'"


def show_changes(data, depth=[]):
    '''function makes raws kind of

    Property '{'.'.join(depth)}' was removed(added, updated)"'''
    result = ''
    for key, value in data.items():
        if not isinstance(value, dict) or value.get('type') == 'no changes':
            continue
        depth.append(key)
        types = ['added', 'removed', 'updated', 'no changes']
        if isinstance(value, dict) and value.get('type') in types:
            type = value['type']
            result += f"Property '{'.'.join(depth)}' was {type}"
            if type == 'added':
                result += f" with value: {normalize(value['value'])}\n"
            elif type == 'removed':
                result += '\n'
            else:
                result += f". From {normalize(value['old_value'])} "
                result += f"to {normalize(value['new_value'])}\n"
        else:
            result += show_changes(value, depth)
        depth.pop()
    return result


def plain_formatter(data):
    '''main function

    cut last\n
    '''
    return show_changes(data)[:-1]
