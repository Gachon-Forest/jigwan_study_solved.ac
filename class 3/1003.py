# Date: 8/9
# No: 1003
# Tier: 실버 3
# Name: 피보나치 함수
# Language: PyPy3
# 주의 : 동적 계획법 활용 (dp)

import sys

t = int(sys.stdin.readline().strip())
dp = [0] * 41

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]
        

for i in range(t):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(fibonacci(n - 1), fibonacci(n))
