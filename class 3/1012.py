# Date: 8/10
# No: 1012
# Tier: 실버 2
# Name: 유기농 배추
# Language: PyPy3
# 주의 : 재귀 깊이가 너무 크게 설정되면 안 되므로 recursion limit을 10,000까지 설정
# 설명 : dfs를 활용하며 방향 설정 후 방문하지 않은 지점부터 dfs 돌기

import sys
sys.setrecursionlimit(10000)

# 방향 벡터 설정
dirR = [1, -1, 0, 0]  # [아래, 위, 오른쪽, 왼쪽]
dirC = [0, 0, 1, -1]

# dfs 함수 정의
def dfs(y, x):
    visited[y][x] = True
    for dirIdx in range(4):
        newY = y + dirR[dirIdx]
        newX = x + dirC[dirIdx]
        if 0 <= newY < n and 0 <= newX < m and graph[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


# t = 테스트 케이스
t = int(sys.stdin.readline().strip())

# 1. 입력 및 초기화
for _ in range(t):
    # m = 배추밭의 가로 길이
    # n = 배추밭의 세로 길이
    # k = 배추가 심어져 있는 위치의 개수
    m, n, k = map(int, sys.stdin.readline().strip().split())

    # 동적으로 그래프 및 방문 배열 생성
    graph = [[False] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    # 1. 그래프 정보 입력
    for _ in range(k):
        # 배추의 위치 좌표
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[y][x] = True

    # 2. 방문하지 않은 지점부터 dfs 돌기
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)