# Date: 8/9
# No: 11726
# Tier: 실버 3
# Name: 2 x n 타일링
# Language: PyPy3
# 주의 : 시간 초과로 인해 리스트 요소 개수가 최대 3개까지밖에 나오지 않으므로 3을 나눠 리스트의 개수를 줄여 출력 시간 줄임
# 설명 : 동적 계획법 활용 (dp) / 패턴 찾기

import sys

n = int(sys.stdin.readline().strip())

arr = [0] * 3
arr[1] = 1
arr[2] = 2

for i in range(3, n + 1):
    arr[i % 3] = (arr[(i - 2) % 3] + arr[(i - 1) % 3]) % 10007
print(arr[n % 3])
