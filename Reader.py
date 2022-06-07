import os


def parse_file(path):
    """Parses a file in a following format:

    n, capacity
    value1, weight1
    value2, weight2
    ...
    valuen, weightn
    """
    value = []
    weight = []
    with open(path, "r") as f:
        n, capacity = tuple(map(int, f.readline().split()))
        for i in range(n):
            v, w = tuple(map(int, f.readline().split()))
            value.append(v)
            weight.append(w)

    return n, value, weight, capacity


def get_optimum(path_to_optima):
    with open(path_to_optima, "r") as f:
        optimum = int(f.readline())
        return optimum


def get_filenames_in_dir(dirpath):
    return os.listdir(dirpath)


if __name__ == '__main__':
    n, value, weight, capacity = parse_file("instances_01_KP/low-dimensional/f1_l-d_kp_10_269")
    print(n, value, weight, capacity)