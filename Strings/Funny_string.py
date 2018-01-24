def funnyString(s):
    # Complete this function
    i = 1
    r = s[::-1]
    f = False
    for i in range(1, len(s)):
        if abs(ord(s[i])-ord(s[i-1])) == abs(ord(r[i])-ord(r[i-1])):
            f = True
        else:
            f = False
            break
    if f == False:
        return 'Not Funny'
    else:
        return 'Funny'


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
