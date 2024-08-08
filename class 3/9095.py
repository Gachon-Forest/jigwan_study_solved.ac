# Date: 8/9
# No: 9095
# Tier: 실버 3
# Name: 1, 2, 3 더하기
# Language: PyPy3
# 주의 : 동적 계획법 활용 (dp)

import sys

t = int(sys.stdin.readline().strip())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for i in range(t):
    n = int(sys.stdin.readline().strip())
    print(dp[n])
