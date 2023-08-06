def handle_command_line(arguments, **defaults_or_types):
    """
    All arguments are keyworded, except boolean ones.

    >>> handle_command_line(["program ···", "start", "end=0", "finish", "n=5", "name=Foo", "lst=a,b,c", "v=0.3"], n=int, start=False, end=bool, lst=list, v=float)
    {'start': True, 'end': False, 'finish': True, 'n': 5, 'name': 'Foo', 'lst': ['a', 'b', 'c'], 'v': 0.3}
    """
    kwargs = {}

    types = defaults_or_types
    for param, value in defaults_or_types.items():
        if not isinstance(value, type):
            types[param] = type(value)
            kwargs[param] = value
    for item in arguments[1:]:
        if "=" in item:
            k, v = item.split("=")
            if k in types:
                if types[k] == int:
                    kwargs[k] = int(v)
                elif types[k] == float:
                    kwargs[k] = float(v)
                elif types[k] == bool:
                    kwargs[k] = bool(int(v))
                elif types[k] == list:
                    kwargs[k] = v.split(",")
                else:  # pragma: no cover
                    raise Exception(f"Unhandled type: `{types[k]}`.")
            else:
                kwargs[k] = v
        else:
            kwargs[item] = True

    return kwargs
