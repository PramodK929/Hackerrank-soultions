def theLoveLetterMystery(s):
    count =0
    for i in range(0, int((len(s)/2))):
        count += abs(ord(s[i])-ord(s[len(s)-1-i]))
    return count
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)