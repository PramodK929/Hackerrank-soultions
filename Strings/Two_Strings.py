p = int(input())
for i in range(p):
    a = input()
    b = input()
    count = 0
    for i in a:
        if i in b:
            count+=1
    print('YES' if count>0 else 'NO')
