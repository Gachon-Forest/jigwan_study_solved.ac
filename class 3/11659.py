# Date: 8/9
# No: 11659
# Tier: 실버 3
# Name: 구간 합 구하기 4
# Language: PyPy3
# 주의 : 동적 프로그래밍 활용(부분합 활용)

import sys

n, m = map(int, sys.stdin.readline().strip().split())

numbers = list(map(int, sys.stdin.readline().strip().split()))

sum_numbers = [0] * (n + 1)

for k in range(1, n + 1):
    sum_numbers[k] = sum_numbers[k - 1] + numbers[k - 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    result = sum_numbers[j] - sum_numbers[i - 1]
    print(result)
