import sys
n, m, k = map(int, input().split(' '))
empty_list = []
arr = [i for i in input().split(' ')]
ones = "1"
time = sys.maxsize
c = 1
prev = -1
for i in range(0, len(arr)):
    if arr[i] == "1":
        empty_list.append(i)
print(empty_list)
if len(empty_list)<m:
    print(-1)
else:
    for i in range(0, len(empty_list)):
        if i == 0:
            prev = 0
        else:
            prev = empty_list[i] - 1
        print(prev)
        count = 0
        t = 0
        j = i
        while(count < m):
            if j == empty_list[0]:
                t += empty_list[j] - prev
                c += 1
            else:
                t += (empty_list[j] - prev) * ( c * k)
                c += 1
            count += 1
            print("inside while: ",count, t)
        time = min(time, t)
    print(time)
