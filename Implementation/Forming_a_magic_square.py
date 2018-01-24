# n = int(input())
a = []
for i in range(3):
    a.append(input().split(' '))
print(a)
row = []
colom = []
dig = []
for i in range(3):
    for j in range(3):
        r = r + int(a[i][j])
        row.append(r)
    c = c + int(a[i][i])
    colom.append(a[i][i])