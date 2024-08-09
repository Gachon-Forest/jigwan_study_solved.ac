# Date: 8/9
# No: 1927
# Tier: 실버 2
# Name: 최소 힙
# Language: PyPy3
# 주의 : 'heapq' 모듈 활용 / 출력 최적화 활용(sys.stdout.write())

import sys
import heapq

n = int(sys.stdin.readline().strip())
arr = []

for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x > 0:
        heapq.heappush(arr, x)
    elif x == 0:
        if len(arr) == 0:
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(heapq.heappop(arr)) + "\n")
