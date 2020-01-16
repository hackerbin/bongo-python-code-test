def recursive_print_depth(data, depth):
    if not isinstance(depth, int):
        raise ValueError("Depth must be Integer")
    for k, v in data.items():
        print("{key} {depth}".format(key=k, depth=depth))
        if isinstance(v, dict):
            recursive_print_depth(v, depth + 1)


def print_depth(data):
    if not isinstance(data, dict):
        raise ValueError("Data must be Dictionary")
    recursive_print_depth(data, 1)


data = {"key1": 1, "key2": {"key3": {"key6": {"key7": 8}, "key8": 9}, "key4": {"key5": 4}}}
print_depth(data)
