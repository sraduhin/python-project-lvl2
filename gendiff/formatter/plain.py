# plain formatter
from gendiff.constrants import (ADDED, REMOVED, UPDATED, CHILDREN,
                                UNCHANGED)


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


def show_changes(data, depth=[]):  # noqa:C901
    '''function makes raws kind of

    Property '{'.'.join(depth)}' was removed(added, updated)"'''
    result = []
    for key, value in sorted(data.items()):
        if not isinstance(value, dict):
            continue
        if value.get('type') == UNCHANGED:
            continue
        depth.append(key)
        if value.get('type') == CHILDREN:
            result.extend(show_changes(value['value'], depth))
            depth.pop()
            continue
        if value.get('type') in [ADDED, REMOVED, UPDATED]:
            type = value['type']
            line = f"Property '{'.'.join(depth)}' was {type}"
            if type == REMOVED:
                result.append(line)
            elif type == ADDED:
                line += f" with value: {normalize(value['value'])}"
                result.append(line)
            else:
                line += f". From {normalize(value['old_value'])} "
                line += f"to {normalize(value['new_value'])}"
                result.append(line)
        else:
            result.append(show_changes(value, depth))
        depth.pop()
    return result


def plain_formatter(data):
    '''main function
    '''
    return '\n'.join(show_changes(data))
