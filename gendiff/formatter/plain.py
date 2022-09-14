def normalize(data):
    if isinstance(data, bool):
        return f'{data}'.lower()
    if isinstance(data, int):
        return data
    if data is None:
        return 'null'
    return '[complex value]' if isinstance(data, dict) else f"'{data}'"


def show_changes(data, depth=[]):
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
            result += show_changes(value, depth)
        depth.pop()
    return result


def main(data):
    return show_changes(data)[:-1]
