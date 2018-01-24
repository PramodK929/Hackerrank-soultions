s = input()
pattern = 'SOS' * len(s)
count = 0
for i in range(0, len(s)):
    if s[i]!=pattern[i]:count+=1
print(count)