# Date: 7/25
# No: 1764
# Tier: 실버 4
# Name: 듣보잡
# Language: PyPy3
# 주의 : 시간 초과 - 리스트 대신 집합 사용

import sys

n, m = map(int, sys.stdin.readline().split())
not_listen = []
not_see = []
result = []
not_listen = set(not_listen)
not_see = set(not_see)
result = set(result)

for i in range(n):
    name1 = sys.stdin.readline().strip()
    not_listen.add(name1)
for i in range(m):
    name2 = sys.stdin.readline().strip()
    not_see.add(name2)

for name in not_listen:
    if name in not_see:
        result.add(name)

result = sorted(result)

print(len(result))
for i in range(len(result)):
    print(result[i])
