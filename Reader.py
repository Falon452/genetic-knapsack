

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


def get_optimum(filename, path_to_optima="optima.csv"):
    with open(path_to_optima, "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            name, optimum = line.split(",")
            if name == filename:
                return optimum

    raise FileNotFoundError("Could not find filename.")


if __name__ == '__main__':
    n, value, weight, capacity = parse_file("problem_instances/n_400_c_1000000_g_2_f_0.1_eps_0_s_100/test.in")
    print(n, value, weight, capacity)