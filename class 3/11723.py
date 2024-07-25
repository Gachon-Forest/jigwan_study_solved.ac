# Date: 7/25
# No: 11723
# Tier: 실버 5
# Name: 집합
# Language: PyPy3
# 주의 : 집합 특징 - 중복된 값 넣어주면 제거됨

import sys

n = int(sys.stdin.readline().strip())
s = []

for i in range(n):
    order = list(sys.stdin.readline().strip().split(" "))
    if 'add' in order:
        s.append(int(order[-1]))
        s = list(set(s))
    elif 'remove' in order:
        if int(order[-1]) not in s:
            continue
        else:
            s.remove(int(order[-1]))
    elif 'check' in order:
        if int(order[-1]) in s:
            print(1)
        else:
            print(0)
    elif 'toggle' in order:
        if int(order[-1]) not in s:
            s.append(int(order[-1]))
        else:
            s.remove(int(order[-1]))
    elif 'all' in order:
        for i in range(1, 21):
            s.append(i)
        s = list(set(s))
    elif 'empty' in order:
        s.clear()
