# Date: 7/17
# No: 2751
# Tier: 실버 5
# Name: 수 정렬하기 2
# Language: PyPy3

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
