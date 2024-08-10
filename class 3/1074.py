# Date: 8/11
# No: 1074
# Tier: 실버 1
# Name: Z
# Language: PyPy3
# 주의 : Z 모양 순서대로 배열을 탐색하여 게산

import sys

# n = 배열의 크기를 결정하는 지수
# r = 행 번호
# c = 열 번호
n, r, c = map(int, sys.stdin.readline().strip().split())

answer = 0

while n != 0:
    n -= 1
    # 제 2사분면
    if r < 2 ** n and c < 2 ** n:
        answer += (2 ** n) * (2 ** n) * 0
    # 제 1사분면
    elif r < 2 ** n and c >= 2 ** n:
        answer += (2 ** n) * (2 ** n) * 1
        c -= (2 ** n)

    # 제 3사분면
    elif r >= 2 ** n and c < 2 ** n:
        answer += (2 ** n) * (2 ** n) * 2
        r -= (2 ** n)

    # 제 4사분면
    else:
        answer += (2 ** n) * (2 ** n) * 3
        r -= (2 ** n)
        c -= (2 ** n)

print(answer)