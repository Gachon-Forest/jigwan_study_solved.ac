# Date: 8/11
# No: 14940
# Tier: 실버 1
# Name: 쉬운 최단거리
# Language: PyPy3
# 주의 : dfs를 활용하여 graph와 visited를 잘 구분하여 기록하는 것이 중요

import sys
# bfs 사용을 위해 deque 모듈 활용
from collections import deque

# n = 세로의 크기, m = 가로의 크기
n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            newX, newY = dx[i] + x, dy[i] + y
            # nx, ny가 범위 내에 있고 visited[nx][ny]가 -1이라면(방문하지 않은 곳이라면)
            if 0 <= newX < n and 0 <= newY < m and visited[newX][newY] == -1:
                # 갈 수 없는 땅(0)과 갈 수 있는 땅(1)에 따라 if문을 걸어줌
                if graph[newX][newY] == 0:
                    visited[newX][newY] = 0
                elif graph[newX][newY] == 1:
                    visited[newX][newY] = visited[x][y] + 1
                    q.append((newX, newY))

# for문을 통해서 목표지점일 때 bfs를 실행
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

# for문을 통해서 visited[i][j]가 -1일 때(방문하지 않았을 때) bfs를 실행
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()