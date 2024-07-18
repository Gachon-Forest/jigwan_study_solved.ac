# Date: 7/18
# No: 9012
# Tier: 실버 4
# Name: 괄호
# Language: PyPy3
# 주의 : 스택 개념 활용
# 리스트 추가, 제거 사용 / '(' 있을 시 리스트 추가, ')' 있을 시 리스트 제거

import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    ps = sys.stdin.readline().strip()
    vps_check = []
    for p in ps:
        if p == '(':
            vps_check.append('(')
        else:
            if len(vps_check) == 0:
                vps_check.append(')')
                break
            else:
                vps_check.pop()

    if len(vps_check) == 0:
        print("YES")
    else:
        print("NO")