from Reader import parse_file
from Dynamic import dynamic_solve
from Genetic import genetic_solve
from OR_Tools import OR_Tools_solve
import time


if __name__ == '__main__':
    n, value, weight, capacity = parse_file("problem_instances/n_400_c_1000000_g_2_f_0.1_eps_0_s_100/test.in")
    print(n, value, weight, capacity)