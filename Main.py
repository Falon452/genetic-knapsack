from Reader import parse_file, get_optimum, get_filenames_in_dir
from Dynamic import dynamic_solve
from Genetic import genetic_solve
from OR_Tools import OR_Tools_solve
from Stats import accuracy
import pandas as pd

from timeit import default_timer as timer
from datetime import timedelta

INPUT_PATH = "instances_01_KP/large_scale/"
OPTIMUM_PATH = "instances_01_KP/large_scale-optimum/"


def compare_algorithms(filenames, save_path):
    data = {'Filename': [],
            'Length': [],
            'DP res': [],
            'OR res': [],
            'Gen res': [],
            'Optimum': [],
            'DP acc': [],
            'OR acc': [],
            'Gen acc': [],
            'DP time': [],
            'OR time': [],
            'Gen time': []}

    for filename in filenames:
        filepath = INPUT_PATH + filename
        optimum_filepath = OPTIMUM_PATH + filename
        data['Filename'].append(filename)
        n, value, weight, capacity = parse_file(filepath)
        data['Length'].append(n)

        optimum = get_optimum(optimum_filepath)
        data['Optimum'].append(optimum)

        # genetic
        start = timer()
        gen_res = genetic_solve(n, value, weight, capacity)
        end = timer()
        data['Gen res'].append(gen_res)
        data['Gen acc'].append(accuracy(gen_res, optimum))
        data['Gen time'].append(timedelta(seconds=end - start).microseconds)

        # dynamic
        start = timer()
        dp_res = dynamic_solve(n, value, weight, capacity)
        end = timer()
        data['DP res'].append(dp_res)
        data['DP acc'].append(accuracy(dp_res, optimum))
        data['DP time'].append(timedelta(seconds=end - start).microseconds)

        # or tools
        start = timer()
        or_res = OR_Tools_solve(n, value, weight, capacity)
        end = timer()
        data['OR res'].append(or_res)
        data['OR acc'].append(accuracy(or_res, optimum))
        data['OR time'].append(timedelta(seconds=end - start).microseconds)

    df = pd.DataFrame(data)
    df = df.round(2)
    df.to_csv(f'{save_path}.csv', index=False)
    return df


# def test_function(n, value, weight, capacity, function):
#     res = None
#     try:
#         with time_limit(MAX_TIME_IN_SEC):
#             res = function(n, value, weight, capacity)
#     except TimeoutException as e:
#         print(f"{function.__name__} timeout after {MAX_TIME_IN_SEC} seconds")
#
#     return res


if __name__ == '__main__':
    df = None
    filenames = get_filenames_in_dir(INPUT_PATH)
    df = compare_algorithms(filenames, "result2")
    print(df)

    # dynamic_res, or_tools_res, genetic_res = None, None, None
    # n, value, weight, capacity = parse_file("instances_01_KP/low-dimensional/f4_l-d_kp_4_11")
    #
    # try:
    #     with time_limit(MAX_TIME_IN_SEC):
    #         dynamic_res = dynamic_solve(n, value, weight, capacity)
    # except TimeoutException as e:
    #     print(f"Dynamic timeout after {MAX_TIME_IN_SEC} seconds")
    #
    # print(dynamic_res)
    # optimum = get_optimum("instances_01_KP/low-dimensional-optimum/f4_l-d_kp_4_11")
    # print(optimum)
    # print(accuracy(dynamic_res, optimum))



