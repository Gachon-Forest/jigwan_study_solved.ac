# Date: 7/25
# No: 11399
# Tier: 실버 4
# Name: ATM
# Language: PyPy3

import sys

n = int(sys.stdin.readline().strip())
time = list(map(int, sys.stdin.readline().split()))
time = sorted(time)
total = 0
sum = 0

for i in time:
    total += i
    sum += total

print(sum)