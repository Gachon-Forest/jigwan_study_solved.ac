# Date: 7/18
# No: 2164
# Tier: 실버 4
# Name: 카드 2
# Language: PyPy3
# 주의 : collections 모듈의 deque 클래스 사용 (시간 초과..)

import sys
from collections import deque

n = int(sys.stdin.readline().strip())
cards = deque()

for i in range(n):
    cards.append(i + 1)

while len(cards) > 1:
    cards.popleft()                 # 1번째 단계
    cards.append(cards.popleft())   # 2번째 단계

print(cards[0])
