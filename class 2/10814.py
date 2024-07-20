# Date: 7/18
# No: 10814
# Tier: 실버 5
# Name: 나이순 정렬
# Language: PyPy3
# 주의 : lambda 함수 적용

import sys

n = int(input())
users = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    users.append((int(age), name))

users.sort(key=lambda x: x[0])

for i in users:
    print(i[0], i[1])