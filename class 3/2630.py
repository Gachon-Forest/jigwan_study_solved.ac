# Date: 8/10
# No: 2630
# Tier: 실버 2
# Name: 색종이 만들기
# Language: PyPy3
# 주의 : 재귀적으로 함수를 호출하면서 그 연산의 단위를 조금씩 줄여가는 방식

import sys

n = int(sys.stdin.readline().strip())                                               # n = 종이의 한 변의 길이
paper = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]    # paper = 0(흰색), 1(파란색)으로 채워진 n * n 크기의 2차원 리스트
result = []                                                                         # 각각의 분할된 영역이 흰색(0)인지 파란색(1)인지 기록하는 리스트

def divide(x, y, n):                                # x, y = 현재 검사 중인 종이의 좌측 상단 좌표 / n = 현재 검사 중인 종이의 크기
    color = paper[x][y]                             # 현재 부분의 첫 번째 칸의 색상을 저장
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                divide(x, y, n//2)
                divide(x, y + n//2, n//2)
                divide(x + n//2, y, n//2)
                divide(x + n//2, y + n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

divide(0, 0, n)     # 전체 종이 영역에서 분할 시작
print(result.count(0))    # 흰색 영역
print(result.count(1))    # 파란색 영역