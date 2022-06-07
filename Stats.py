

def accuracy(observed, true):
    if not observed:
        print("observed is None")  # probably due to timeout
        return 0
    if not true:
        raise ValueError("true is None")
    return 100 - abs((observed - true)/true) * 100


if __name__ == '__main__':
    print(accuracy(2333, 2332))
    print(accuracy(None, 2332))
    assert accuracy(323, 323) == 100