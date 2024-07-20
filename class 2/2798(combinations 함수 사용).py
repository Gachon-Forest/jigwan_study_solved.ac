# Date: 3/31
# No: 2798
# Tier: 브론즈 2
# Name: 블랙잭
# Language: PyPy3

import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

if 3 <= n <= 100 and 10 <= m <= 300000:
    cards = list(map(int, sys.stdin.readline().split()))

    all = combinations(cards, 3)  # 3개의 숫자를 합한 값을 구하는 모든 경우의 수

    valid = []  # 주어진 수 m보다 작거나 같은 모든 경우의 수
    for i in all:
        if sum(i) <= m:
            valid.append(sum(i))

    sum_list = [sum(i)]

    if valid:
        print(max(valid))
