# Date: 7/16
# No: 1546
# Tier: 브론즈 1
# Name: 평균
# Language: PyPy3

n = int(input(""))
scores = list(map(int, input("").split()))
max_score = max(scores)

for i in range(n):
    scores[i] = scores[i] / max_score * 100

print(sum(scores) / n)
