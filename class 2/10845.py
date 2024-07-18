# Date: 7/18
# No: 10845
# Tier: 실버 4
# Name: 큐
# Language: PyPy3

import sys
from collections import deque

n = int(sys.stdin.readline())
queue = []

for i in range(n):
    order = sys.stdin.readline().strip()

    if order.startswith('push'):
        i, value = order.split()
        queue.append(int(value))
    elif order == 'pop':
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif order == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
