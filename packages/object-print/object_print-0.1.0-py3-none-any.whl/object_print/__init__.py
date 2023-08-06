def _tree_recurse(obj, indent, prefix='', suffix=''):
    spaces = ' ' * indent
    match obj:
        case list() if len(obj) == 0:
            print(spaces + prefix + "[]" + suffix)
        case list() if len(obj) == 1:
            if issubclass(type(obj[0]), (type(dict()), type(list()))):
                print(spaces + prefix + "[")
                _tree_recurse(obj[0], indent+1, suffix=',')
                print(spaces + "]" + suffix)
            else:
                print(spaces + prefix + f"[{repr(obj[0])}]" + suffix)
        case list():
            print(spaces + prefix + "[")
            for item in obj:
                _tree_recurse(item, indent+1, suffix=',')
            print(spaces + "]" + suffix)
        case dict() if len(obj) == 0:
                print(spaces + prefix + "{}" + suffix)
        case dict() if len(obj) == 1:
            key = list(obj)[0]
            val = obj[key]
            if issubclass(type(val), (type(dict()), type(list()))):
                print(spaces + prefix + "{")
                _tree_recurse(val, indent+1, prefix=repr(key) + ': ', suffix=',')
                print(spaces + '}' + suffix)
            else:
                print(spaces + prefix + "{ " + repr(key) + ': ' + repr(val) + " }" + suffix)
        case dict():
            print(spaces + prefix + "{")
            for key, val in obj.items():
                _tree_recurse(val, indent+1, prefix=str(repr(key)) + ': ', suffix=',')
            print(spaces + '}' + suffix)
        case int():
            print(spaces + prefix + str(obj) + suffix)
        case str():
            print(spaces + prefix + f"'{obj}'" + suffix)
        case _:
            print(spaces + prefix + f"?? {obj} ??" + suffix)


def object_print(root):
    _tree_recurse(root, 0)


if __name__ == '__main__':
    object_print({'a': 1, 'b': 2})
    object_print([1, 2, 3])
    object_print(1)

    object_print([
        'a',
        {
            'foo': 'bar',
            1: 23,
            'nest0': [],
            'nest1': [0],
            'nest2': [1, 2],
            'nestdict0': {},
            'nestdict1': {'k': 'v'},
            'nestdict2': {'k': 'v', 'k2': 'v2'},
        },
        ['nested', ['lists', ['r', ['fun']]]],
        [[[['nested'], 'lists'], 'r'], 'fun'],
    ])
