n = int(input())
arr = [int(i) for i in input().split(' ')]
konda = arr[-1]
for i in range(n-2, -1, -1):
    if arr[i] > konda:
        arr[i+1] = arr[i]
    else:
        arr[i+1] = konda
        break
    print(" ".join(str(x) for x in arr))
if arr[0] > konda:
    arr[0] = konda
print(" ".join(str(x) for x in arr))