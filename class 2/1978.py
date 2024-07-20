# Date: 7/11
# No: 1978
# Tier: 브론즈 2
# Name: 소수 찾기
# Language: PyPy3

import sys

def prime_number(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, x):
        if x % i == 0:
            return False
    return True

n = int(input(""))
numbers = list(map(int, sys.stdin.readline().split()))

count = 0
for number in numbers:
    if prime_number(number) == True:
        count += 1

print(count)