# 338. Counting Bits
# Given an integer n, return an array ans of length n + 1
# such that for each i (0 <= i <= n), ans[i] is
# the number of 1's in the binary representation of i.
def countBits(n: int):
    dp = [0]
    for i in range(1, n + 1):
        if i % 2 == 1:
            dp.append(dp[i - 1] + 1)
        else:
            dp.append(dp[i // 2])

    return dp


# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


def generate_pascal_triangle(numRows: int):
    dp = [[1]]
    for i in range(1, numRows):
        tmp = [1]
        for j in range(1, i):
            tmp.append(dp[i - 1][j - 1] + dp[i - 1][j])
        tmp.append(1)
        dp.append(tmp)

    return dp


# 509. Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
def fib(n: int):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


def fib_rec(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


# 1137. N-th Tribonacci Number
def tribonacci(n: int):
    dp = [0, 1, 1]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    return dp[n]


# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def maxProfit(prices):
    dp = [0] * (len(prices))
    hold = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < hold:
            hold = prices[i]

        dp[i] = max(dp[i - 1], prices[i] - hold)
    return dp[-1]


# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def climbStairs(n: int):
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


# 746. Min Cost Climbing Stairs
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
def minCostClimbingStairs(cost):
    dp = [0] * len(cost)
    if not cost:
        return 0

    dp[0] = cost[0]
    if len(cost) >= 2:
        dp[1] = cost[1]

    for i in range(2, len(cost)):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[-1], dp[-2])


# 1646. Get Maximum in Generated Array
# You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:
# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# Return the maximum integer in the array nums​​​.
def getMaximumGenerated(n):
    if not n:
        return 0
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = dp[i // 2]
        else:
            dp[i] = dp[i // 2] + dp[(i // 2) + 1]
    return max(dp)


if __name__ == "__main__":
    print(getMaximumGenerated(4))
