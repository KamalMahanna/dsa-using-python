def min_cost(cost, n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return cost[0]

    if n == 1:
        return cost[1]

    memo[n] = cost[n] + min(min_cost(cost, n - 1, memo), min_cost(cost, n - 2, memo))

    return memo[n]


print(min_cost([10, 15, 20], 2))
print(min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 9))


def minCostClimbingStairs(cost):
    n = len(cost)
    return min(min_cost(cost, n - 1), min_cost(cost, n - 2))


print(minCostClimbingStairs([10, 15, 20]))
