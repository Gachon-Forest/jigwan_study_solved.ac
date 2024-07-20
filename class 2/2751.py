# Date: 7/17
# No: 2609
# Tier: 브론즈 1
# Name: 최대공약수와 최소공배수
# Language: PyPy3
# 주의 : math 모듈 사용하여 최대공약수를 'gcd'함수를, 최소공배수를 'lcm'함수를 사용

# 1번째 방법
import sys

n = sys.stdin.readline()
numbers = []

for i in range(int(n)):
    number = sys.stdin.readline()
    numbers.append(int(number))

numbers_list = list(set(numbers))
numbers_list.sort()

for i in range(len(numbers_list)):
    print(numbers_list[i])
    i += 1

# 2번째 방법
n = int(input(""))
numbers = []

for i in range(n):
    number = int(input(""))
    numbers.append(number)

numbers_list = list(set(numbers))
numbers_list.sort()

for i in range(len(numbers_list)):
    print(numbers_list[i])
    i += 1
