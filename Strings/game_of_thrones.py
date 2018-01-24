def gameOfThrones(s):
    a = "".join(s)
    b = []
    count = 0
    result = False
    for i in range(0, len(a)):
        if a[i] not in b:b.append(a[i])
    for i in b:
        if s.count(i)%2 == 0:result = True
        else:count+=1
    if result == True and count<2:return 'YES'
    else: return 'NO'
s = input().strip()
result = gameOfThrones(s)
print(result)
