# Date: 7/19
# No: 1018
# Tier: 실버 4
# Name: 체스판 다시 칠하기
# Language: PyPy3
# 주의 : 시작 지점을 검은색, 흰색일 경우 2가지로 분류 후 변수 2개 설정
# board[a][b] 지점을 2로 나누었을 때 나머지가 0일 때와 1일 때를 이용하여 어느 색을 칠할지 결정

import sys

n, m = map(int, sys.stdin.readline().split())
board = []
result = []

for i in range(n):
    lines = sys.stdin.readline().strip()
    board.append(lines)

for i in range(n - 7):
    for j in range(m - 7):
        color1 = 0
        color2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        color1 += 1
                    if board[a][b] != 'W':
                        color2 += 1
                else:
                    if board[a][b] != 'W':
                        color1 += 1
                    if board[a][b] != 'B':
                        color2 += 1
        result.append(color1)
        result.append(color2)

print(min(result))
