# Date: 8/9
# No: 11726
# Tier: 실버 2
# Name: 연결 요소의 개수
# Language: PyPy3
# 주의 : 깊이 우선 탐색 함수 활용
# 설명 : 모든 노드를 순회하면서 방문되지 않은 노드를 발견하면 그 노드를 시작으로 DFS를 수행하여 연결된 모든 노드를 방문

import sys

# g = 그래프(graph)
# v = 현재 탐색 중인 노드의 인덱스(visit)
# visited = 노드가 방문되었는지를 기록하는 리스트
def dfs(g, v, visited):
    visited[v] = True           # 현재 노드 v를 방문했다고 표시
    for i in g[v]:              # g[v] = 노드 v와 연결된 모든 이웃 노드들의 리스트
        if not visited[i]:      # 이웃 노드 i가 아직 방문되지 않은 경우
            dfs(g, i, visited)

n, m = map(int, sys.stdin.readline().strip().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0                       # 여결 요소의 개수
visited = [False] * (n + 1)     # 각 노드의 방문 여부를 기록하는 리스트
for i in range(1, n + 1):
    if not visited[i]:          # 노드 i가 방문되지 않은 경우
        dfs(graph, i, visited)  # 노드 i를 시작으로 깊이 우선 탐색 수행하여 연결된 모든 노드 방문
        count += 1              # 새로운 연결 요소 발견할 때마다 카운트 증가

print(count)
