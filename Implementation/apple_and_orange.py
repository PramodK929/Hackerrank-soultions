s, t =input().split(' ')
a, b = input().split(' ')
m, n = input().split(' ')
ma = [int(i) for i in input().split(' ')]
nb = [int(i) for i in input().split(' ')]
count = 0
for i in ma[:]:
    if int(a) + i >= int(s) and int(a) + i <= int(t):
        count+=1
print(count)
count = 0
for i in nb[:]:
    if int(b) + i >= int(s) and int(b) + i <= int(t):
        count+=1
print(count)


