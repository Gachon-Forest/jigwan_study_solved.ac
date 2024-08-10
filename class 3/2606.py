# Date: 8/10
# No: 2606
# Tier: 실버 3
# Name: 바이러스
# Language: PyPy3
# 주의 : dfs(깊이 우선 탐색) 활용

import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)     # a에 b를 연결
    graph[b].append(a)     # b에 a를 연결 → 양방향

def dfs(x):
    stack = [x]                         # 탐색 시작할 노드 'x'를 스택에 넣음
    visited[x] = True                   # 시작 노드 'x'를 방문함
    count = 0                           # 방문한 노드의 개수 초기화
    while stack:                        # 스택이 비어있지 않을 때까지 탐색 진행
        node = stack.pop()              # 스택의 맨 위 노드 꺼내서 현재 탐색 중인 'node로 설정
        for next in graph[node]:        # 노드에 연결된 모든 이웃한 노드 'next' 탐색
            if not visited[next]:       # 이웃 노드 'next'가 아직 방문되지 않았을 경우
                visited[next] = True    # 이웃 노드 'next'를 방문했다고 표시
                stack.append(next)      # 이웃 노드 'next'를 스택에 추가하여 나중에 탐색할 수 있도록 함
                count += 1              # 방문한 노드의 개수 + 1
    return count

print(dfs(1))