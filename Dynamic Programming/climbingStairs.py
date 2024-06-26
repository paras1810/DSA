def climbCount(n):
    dp = [0 for x in range(n+1)]
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

if __name__ == "__main__":
    n = 4
    res = climbCount(n)
    print(res)