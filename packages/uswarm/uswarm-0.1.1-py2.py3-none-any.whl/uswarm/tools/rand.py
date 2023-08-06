"""Helpers for dealing with random values generation.

Random Samples
-----------------------

- [x] random names and values.
- [x] random populatd containers.



"""

# -----------------------------------------------------------
# random strings, values and containers
# -----------------------------------------------------------


def random_name(size=10, mixed_case=False, first_letter=True):
    if mixed_case:
        domain = string.digits + string.ascii_lowercase + string.ascii_uppercase + "_"
    else:
        domain = string.digits + string.ascii_lowercase + "_"

    result = "".join(random.choice(domain) for _ in range(size))
    if first_letter:
        result = random.choice(domain[10:]) + result[1:]
    return result


def random_value(size=10, options=[str, bytes, int, float, bool]):
    t = random.choice(options)

    # try to expand type 't'
    if t == str:
        domain = string.digits + string.ascii_letters + "_"
        return "".join(random.choice(domain) for _ in range(size))
    if t == bytes:
        result = "".join([chr(random.randint(0, 255)) for _ in range(size)])
        return bytes(result, "utf-8")
    if t == int:
        return random.randint(-size, +size)
    if t == float:
        return (random.random() - 0.5) * size * 2
    if t == bool:
        return random.choice([True, False])

    if t == "date":  # preserve some fields
        return datetime.now().replace(
            month=random.randint(1, 12),
            day=random.randint(1, 28),
            hour=random.randint(0, 23),
            minute=random.randint(0, 59),
        )
    # otherwise return the option
    return t


def random_dict(length=20, size=10, options=[str, bytes, int, float, bool]):
    result = dict()
    for _ in range(length):
        key = random_name()
        value = random_value(size=size, options=options)
        result[key] = value
    return result


def random_specific_dict(**pattern):
    result = dict()
    for name, klass in pattern.items():
        if isinstance(klass, (list, tuple, set)):
            result[name] = random_value(options=klass)
        else:
            result[name] = random_value(options=[klass])
    return result
