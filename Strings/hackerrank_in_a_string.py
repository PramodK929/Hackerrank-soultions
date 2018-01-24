q = int(input().strip())
hackerrank = 'hackerrank'
for inp in range(q):
    j = 1
    k = 0
    result = False
    s = input().strip()
    for i in range(0, len(hackerrank)):
        for j in range(k, len(s)):
            if hackerrank[i] == s[j]:
                result = True
                break
            else:
                result = False
        if result == False:
            break
        k = j
    if result == True:
        print('YES')
    else:
        print('NO')


