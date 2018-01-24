s, n, m = input().split(' ')
a = [int(i) for i in input().split(' ')]
b = [int(i) for i in input().split(' ')]
c = []
flag = False
for i in range(0, int(n)):
    for j in range(0, int(m)):
        if (a[i] + b[j]) <= (int(s)):
            c.append(a[i] + b[j])
            flag = True
if flag:
    print(max(c))
else:
    print(-1)