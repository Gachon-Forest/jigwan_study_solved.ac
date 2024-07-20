# Date: 7/18
# No: 11866
# Tier: 실버 5
# Name: 요세푸스 문제 0
# Language: PyPy3
# 주의 : 리스트 요소 개수 활용

import sys

n, k = map(int, sys.stdin.readline().split())

index = 0
people = []
result = []

for i in range(n):
    people.append(i + 1)

while len(people) > 0:
    index += (k - 1)
    index %= len(people)
    result.append(people.pop(index))

print("<", end = "")
for i in range(n - 1):
    print(result[i], end = ", ")
print(result[n - 1], end = "")
print(">", end = "")