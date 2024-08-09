# Date: 8/9
# No: 18870
# Tier: 실버 2
# Name: 좌표 압축
# Language: PyPy3
# 주의 : 리스트와 딕셔너리 활용

import sys

n = int(sys.stdin.readline().strip())
x_list = list(map(int, sys.stdin.readline().strip().split()))
sorted_x_list = sorted(list(set(x_list)))

position = {sorted_x_list[i] : i for i in range(len(sorted_x_list))}

for i in x_list:
    print(position[i], end=" ")
