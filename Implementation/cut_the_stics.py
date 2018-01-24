n = int(input())
a = [int(i) for i in input().strip().split(' ')]
length = len(a)
small = min(a)
while length != 0:
    count = 0
    b = []
    x = 0
    for i in a[:]:
        if i >= small:
            x = i-small
            count += 1
            if x > 0:b.append(int(x))
    print(count)
    a = b
    length = len(b)
    if len(b)>0:small = min(b)