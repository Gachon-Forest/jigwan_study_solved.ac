# Date: 7/11
# No: 1181
# Tier: 실버 5
# Name: 단어 정렬
# Language: PyPy3

import sys

n = int(sys.stdin.readline())
words_list = []

for i in range(n):
    words = input("")
    words_list.append(words)

result = list(set(words_list))

result.sort()
result.sort(key = lambda x : len(x))

for word in result:
    print(word)
