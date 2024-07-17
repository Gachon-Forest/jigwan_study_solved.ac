// 백준 2562번
number = []
for i in range(9):
    a = int(input())
    number.append(a)
print(max(number))
print(number.index(max(number)) + 1)
