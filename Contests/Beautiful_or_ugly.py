q = int(input())
for i in range(q):
    n = int(input())
    arr = [int(i) for i in input().split(' ')]
    st = set(arr)
    mx = max(arr)
    mn = min(arr)
    if len(st) == len(arr) and mn == 1 and mx == n and (arr[0] != 1 or arr[-1] != n):
        print("Beautiful")
    else:
        print("Ugly")

