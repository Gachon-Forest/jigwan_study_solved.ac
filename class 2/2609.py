# Date: 7/17
# No: 2609
# Tier: 브론즈 1
# Name: 최대공약수와 최소공배수
# Language: PyPy3
# 주의 : math 모듈 사용하여 최대공약수를 'gcd'함수를, 최소공배수를 'lcm'함수를 사용

import sys
import math

n1, n2 = map(int, sys.stdin.readline().split())

print(math.gcd(n1, n2))
print(math.lcm(n1, n2))
