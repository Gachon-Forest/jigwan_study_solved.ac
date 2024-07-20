# Date: 7/11
# No: 30802
# Tier: 브론즈 3
# Name: 웰컴 키트
# Language: PyPy3

import sys
import math

# n = 참가자의 수
n = int(input(""))
# S, M, L, XL, XXL, XXXL = 티셔츠 사이즈별 신청자의 수
S, M, L, XL, XXL, XXXL = map(int, sys.stdin.readline().split())
# t = 티셔츠의 묶음 수, p = 펜의 묶음 수
t, p = map(int, sys.stdin.readline().split())

sizes = [S, M, L, XL, XXL, XXXL]

tshirts_set = 0
for size in sizes:
    tshirts_set += math.ceil(size/t)    # math.ceil() : 올림 함수
pen_set = n // p
pen_piece = n % p

print(tshirts_set)
print(pen_set, pen_piece)