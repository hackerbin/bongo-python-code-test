class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def recursive_print_depth(data, depth):
    if not isinstance(depth, int):
        raise ValueError("Depth must be Integer")

    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, Person):
                print("{key}: {depth}".format(key=k, depth=depth))
            else:
                print("{key} {depth}".format(key=k, depth=depth))
            if isinstance(v, Person) or isinstance(v, dict):
                recursive_print_depth(v, depth + 1)
    else:
        for k, v in data.__dict__.items():
            print("{key}: {depth}".format(key=k, depth=depth))
            if isinstance(v, Person) or isinstance(v, dict):
                recursive_print_depth(v, depth + 1)


def print_depth(data):
    if not (isinstance(data, dict) or isinstance(data, Person)):
        raise ValueError("Data must be Dictionary or Person")
    recursive_print_depth(data, 1)


person_a = Person("a", "b", None)
person_b = Person("a", "b", person_a)

data = {"key1": 1, "key2": {"key3": 1, "key4": {"key5": 4, "user": person_b}}}
print_depth(data)
