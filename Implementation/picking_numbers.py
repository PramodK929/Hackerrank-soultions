n = int(input())
a = [int(i) for i in input().split(' ')]
a = sorted(a)
m = 0
for i in range(0, n-1):
    d = []
    for j in range(i+1, n):
        if abs(a[i] - a[j]) <= 1: d.append(a[i])
    if len(d) >= m: m = len(d)
print(m+1)
# reduce(lambda y, x:max(arr[x] + arr[x + 1], y), range(100), -1)