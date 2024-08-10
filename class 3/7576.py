# Date: 8/11
# No: 7576
# Tier: 골드 5
# Name: 토마토
# Language: PyPy3
# 주의 : dfs 활용 및 방향 리스트 등을 2차원 배열로 사용

import sys
from collections import deque

# 가로, 세로 길이 (m, n)
m, n = map(int, sys.stdin.readline().strip().split())
box = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

q = deque()

# 방향 리스트 [dx[0], dy[0]]은 [-1, 0]이므로 왼쪽으로 이동하는 위치
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 정답 변수
answer = 0

# q에 처음에 받은 토마토의 위치 좌표를 추가
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        # 처음 토마토 좌표 x, y 꺼냄
        x, y = q.popleft()
        # 처음 토마토 사분면의 익을 토마토를 확인
        for i in range(4):
            next_x, next_y = dx[i] + x, dy[i] + y
            # 해당 좌표가 좌표 크기를 넘어가면 안 되고, 그 좌표에 토마토가 익지 않은 채로 있어하 함
            if 0 <= next_x < n and 0 <= next_y < m and box[next_x][next_y] == 0:
                box[next_x][next_y] = box[x][y] + 1
                q.append([next_x, next_y])

bfs()
for i in box:
    for j in i:
        # 다 찾아봤을 때 토마토를 익히지 못 했을 경우 -1 출력
        if j == 0:
            print(-1)
            exit(0)
        # 전부 익혔디면 최댓값이 답이 됨
    answer = max(answer, max(i))

# 처음 시작을 1로 표현하였으므로 1을 빼줌
print(answer -1)