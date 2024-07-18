# Date: 7/18
# No: 1920
# Tier: 실버 4
# Name: 수 찾기
# Language: PyPy3
# 주의 : 리스트 'a'를 'set'(집합)으로 변경하면 시간 복잡도가 'O(n * m)'에서 'O(n + m)'으로 줄어들어 시간 초과 해결 가능

import sys

n = int(sys.stdin.readline().strip())
a = set(sys.stdin.readline().split())
m = int(sys.stdin.readline().strip())
b = sys.stdin.readline().split()

for number in b:
    if number in a:
        print(1)
    else:
        print(0)
