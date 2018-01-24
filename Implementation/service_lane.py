n, t = map(int, input().split(' '))
arr = [int(i) for i in input().split(' ')]
result = []
for i in range(t):
    mn, mx = map(int, input().split(' '))
    result.append(min(arr[mn:mx+1]))
for k in result:
    print(k)