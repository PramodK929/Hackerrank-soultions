t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n),int(k)]
    no = 0
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    for element in a[:]:
        if element <= 0 :
            no += 1
    if no >= k:
        print("NO")
    else:
        print("YES")