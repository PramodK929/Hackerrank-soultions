q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    for i in range(1, len(s)):
        int(s[i]+s[i-1])