from Reader import parse_file, get_optimum
from Dynamic import dynamic_solve
from Genetic import genetic_solve
# from OR_Tools import OR_Tools_solve
from TimeLimit import time_limit, TimeoutException
from Stats import relative_error
import time

MAX_TIME_IN_SEC = 2

if __name__ == '__main__':
    dynamic_res, or_tools_res, genetic_res = None, None, None
    n, value, weight, capacity = parse_file("problem_instances/n_400_c_1000000_g_2_f_0.1_eps_0_s_100/test.in")

    try:
        with time_limit(MAX_TIME_IN_SEC):
            dynamic_res = dynamic_solve(n, value, weight, capacity)
    except TimeoutException as e:
        print(f"Dynamic timeout after {MAX_TIME_IN_SEC} seconds")

    print(dynamic_res)
    optimum = get_optimum("n_400_c_1000000_g_2_f_0.1_eps_0_s_100")
    print(optimum)
    print(relative_error(dynamic_res, optimum))
