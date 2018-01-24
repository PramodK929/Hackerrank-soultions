n, k = map(int, input().split())
arr = [int(i) for i in input().split(' ')]
count = 0
refresh = False
page = 1
for i in arr:
    for j in range(1, i+1):
            if j == page:count += 1
            if j % k == 0:
                page += 1
                refresh = True
            else:refresh = False
    if refresh == False:page += 1
print(count)