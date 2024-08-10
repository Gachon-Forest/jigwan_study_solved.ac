# Date: 8/10
# No: 1697
# Tier: 실버 1
# Name: 숨바꼭질
# Language: PyPy3
# 주의 : bfs(너비 우선 탐색) 활용
# 설명 : 딕셔너리, 집합보다 값을 많이 사용할 수 있는 리스트 활용

import sys
from collections import deque

# n = 수빈 위치 / k = 동생 위치
n, k = map(int, sys.stdin.readline().strip().split())

visited = [0] * (100000 + 1)            # 각 위치 방문 여부 리스트 초기화

def bfs(s):
    q = deque()                         # 빈 큐 생성
    q.append(s)                         # 시작 위치를 큐에 추가
    while q:
        cur = q.popleft()               # 큐에서 현재 위치 'cur' 꺼냄
        if cur == k:
            return visited[k]           # 현재 위치가 목표 위치 'k'와 같다면 목표 위치까지의 최소 이동 횟수(visited[k)를 반환
        for i in (cur + 1, cur - 1, cur * 2):   # 3가지 경우 검사
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[cur] + 1
                q.append(i)             # 다음 위치 i를 큐에 추가하여 나중에 탐색할 수 있도록 함
print(bfs(n))
