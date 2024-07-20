# Date: 7/18
# No: 11650
# Tier: 실버 5
# Name: 좌표 정렬하기
# Language: PyPy3
# 주의 : 리스트 제 적소에 활용

import sys

n = int(sys.stdin.readline())
xy = []

for i in range(n):
    xi, yi = map(int, sys.stdin.readline().split())
    xy.append([xi, yi])

xy.sort()

for i in xy:
    print(i[0], i[1])