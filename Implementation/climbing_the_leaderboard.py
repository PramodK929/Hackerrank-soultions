n = int(input())
score = [int(i) for i in input().split(' ')]
m = int(input())
alia_score = [int(i) for i in input().split(' ')]
ascore = sorted(set(score))
abscore = ascore[::-1]
result = abscore
print(abscore)
print(alia_score)
j = len(abscore)-1
for i in alia_score[:]:
    if i< abscore[-1]:
        # print(j+2)
        result.append(i)
        # print(result.append(i))
    while i > abscore[j] and j > 0:
        j-=1
    result.insert(j, i)
    # print(result.append(j))
ax = set(result)
az = sorted(ax)
print(sorted(ax))