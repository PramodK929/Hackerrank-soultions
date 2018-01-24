n = int(input())
a = [int(i) for i in input().split(' ')]
ind = []
ref = int(len(a))-1
j = 0
for i in range(0, int(len(a)/2), 1):
    flag = True
    for j in range(ref, int(len(a)/2)-1, -1):
        if a[i] == a[j] and flag:
            ind.append(abs(i-j))
            break
        else:break
    ref = j-1
if len(ind)>0:
    print(min(ind))
else:
    print(-1)

