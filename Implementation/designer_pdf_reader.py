a = [int(i) for i in input().split(' ')]
s = input()
ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
m = 0
for i in range(0, len(s)):
    if a[ch.index(s[i])] >= m: m = a[ch.index(s[i])]
print(m*len(s))