# Date: 7/17
# No: 11050
# Tier: 브론즈 1
# Name: 이항 계수 1
# Language: PyPy3
# 주의 : 수학 공식(팩토리얼) 사용

import sys

n, k = map(int, sys.stdin.readline().split())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(n) // (factorial(n - k) * factorial(k)))