# Date: 7/18
# No: 10816
# Tier: 실버 4
# Name: 숫자 카드 2
# Language: PyPy3
# 주의 : collections 모듈의 counter 클래스 사용 (시간 초과 발생..)

import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
first_numbers = sys.stdin.readline().split()
m = int(sys.stdin.readline().strip())
second_numbers = sys.stdin.readline().split()

counter = Counter(first_numbers)

for number in second_numbers:
    print(counter[number], end=" ")
