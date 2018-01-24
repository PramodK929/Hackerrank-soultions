n, d = map(int, input().split(' '))
arr = [int(i) for i in input().split(' ')]
count = 0
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[j] - arr[i] == d and arr[k] - arr[j]==d:
                count += 1
print(count)
