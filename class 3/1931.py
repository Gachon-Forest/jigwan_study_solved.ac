# Date: 8/9
# No: 1931
# Tier: 실버 1
# Name: 회의실 배정
# Language: PyPy3
# 주의 : 회의 시작 시간 빠른 것, 회의 끝나는 시간 빠른 것 오름차순으로 정렬

import sys
n = int(sys.stdin.readline().strip())
time = []

for i in range(n):
    start, end = map(int, sys.stdin.readline().strip().split())
    time.append((start, end))

time.sort(key = lambda x : (x[1], x[0]))

count = 1
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]

print(count)