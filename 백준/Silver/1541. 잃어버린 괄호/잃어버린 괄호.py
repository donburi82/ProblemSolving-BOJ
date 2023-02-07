import sys

expressions = list(sys.stdin.readline().strip().split('-'))
answer = 0
for i in range(len(expressions)):
    exp = expressions[i]
    temp = sum(map(int, exp.split('+')))
    if i==0:
        answer += temp
    else:
        answer -= temp
print(answer)