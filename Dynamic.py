from TimeLimit import *
from Settings import MAX_TIME_IN_SEC

def dynamic_solve(n, value, weight, capacity):
    dp = [0 for i in range(capacity + 1)]  # Making the dp array
    try:
        with time_limit(MAX_TIME_IN_SEC):
            for i in range(1, n + 1):  # taking first i elements
                for w in range(capacity, 0, -1):  # starting from back,so that we also have data of
                    # previous computation when taking i-1 items
                    if weight[i - 1] <= w:
                        # finding the maximum value
                        dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])

            return dp[capacity]  # returning the maximum value of knapsack
    except TimeoutException as e:
        print("timeout!")
        return max(dp)

if __name__ == '__main__':
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    assert dynamic_solve(n, val, wt, W) == 220
