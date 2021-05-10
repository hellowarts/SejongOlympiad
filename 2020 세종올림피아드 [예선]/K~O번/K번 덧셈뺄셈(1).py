n = int(input())
nums = list(map(int,input().split()))

dp = []
for i in range(n-1):
    dp.append([0 for _ in range(21)])

dp[0][nums[0]] = 1
for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j] != 0:
            prev = j
            next_ = nums[i]
            if 0 <= prev + next_ <= 20:
                dp[i][prev+next_] += dp[i-1][prev]
            if 0 <= prev - next_ <= 20:
                dp[i][prev-next_] += dp[i-1][prev]

print(dp[n-2][nums[n-1]])
