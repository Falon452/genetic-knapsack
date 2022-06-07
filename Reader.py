

def parse_file(path):
    """Parses a file in a following format:

    3
    1 3 8
    2 2 8
    3 9 1
    10

    3 - number of items
    1 3 8 - 1 is ID, 3 is value, 8 is weight
    ...
    10 - backpack_capacity
    """
    value = []
    weight = []
    with open(path, "r") as f:
        n = int(f.readline().strip())
        for i in range(n):
            id, v, w = tuple(map(int, f.readline().split()))
            value.append(v)
            weight.append(w)

        capacity = int(f.readline())

    return n, value, weight, capacity
