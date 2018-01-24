n = int(input())
score = [int(i) for i in input().split(' ')]
m = int(input())
a = []
z = []
alia_score = [int(i) for i in input().split(' ')]
a = score + alia_score
b = sorted(a)
count = 1
m = max(b)
for i in b[::-1]:
     if i >= m:
        z.append(count)
     else:
        count += 1
        z.append(count)
        m = i
p = 1
q = 0
x = z[::-1]
print(x)
print(b)
for i in range(0, len(x)+1):
    if alia_score[q] == b[i] and q<=len(alia_score):
