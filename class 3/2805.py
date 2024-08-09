# Date: 8/9
# No: 2805
# Tier: 실버 2
# Name: 나무 자르기
# Language: PyPy3
# 주의 : 이진 탐색 활용
# 설명 : 이진 탐색 진행하면서 start, end가 좁혀지면서 최종적으로 하나의 값에 수렴되므로 높이의 최댓값인 end를 출력

import sys

n, m = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

# 가장 짧은 길이 1을 start, 가장 긴 길이 end 설정
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    log = 0

    for i in trees:
        if i > mid:
            log += i - mid
    # 벌목나무가 목표치 이상일 경우
    if log >= m:
        start = mid + 1
    # 벌목나무가 목표치 이하일 경우
    else:
        end = mid - 1
print(end)