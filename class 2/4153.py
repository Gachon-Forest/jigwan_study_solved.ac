# Date: 7/11
# No: 4153
# Tier: 브론즈 3
# Name: 직각삼각형
# Language: PyPy3

import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    if (pow(a, 2) + pow(b, 2) == pow(c, 2)) or (pow(b, 2) + pow(c, 2) == pow(a, 2)) or (pow(c, 2) + pow(a, 2) == pow(b, 2)):
        print("right")
    else:
        print("wrong")
