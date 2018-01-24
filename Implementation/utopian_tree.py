t = int(input())
a = []
for i in range(t):
    ip = int(input())
    height = 1
    for i in range(1, ip+1):
        if i % 2 != 0:height = 2 * height
        else: height += 1
    print(height)
