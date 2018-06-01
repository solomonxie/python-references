"""
Dynamic Programming (DP) solves complex problems by breaking them down into simpler subproblems and storing their results.
It is particularly effective for problems with overlapping subproblems and optimal substructure, such as calculating Fibonacci numbers.
"""


def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


if __name__ == "__main__":
    print(f"Fibonacci(10): {fibonacci(10)}")
