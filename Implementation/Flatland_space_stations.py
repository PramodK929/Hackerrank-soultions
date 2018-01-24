n, m = map(int, input().split(' '))
a = [int(i) for i in input().split(' ')]
arr = sorted(a)
mx = 0
global_minimum = max(abs(0-arr[0]), abs(arr[-1]-(n-1)))
for i in range(0, m-1):
    diff = (arr[i+1]-arr[i])//2
    if diff > global_minimum:
        global_minimum = diff
print(global_minimum)