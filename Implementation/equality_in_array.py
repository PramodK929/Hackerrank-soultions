n = int(input())
a = [int(i) for i in input().split(' ')]
m = 0
for i in a[:]:
    ele = a.count(i)
    if ele >= m:
        m = ele
print(abs(len(a)-m))