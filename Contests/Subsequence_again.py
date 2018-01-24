s = input()
k = int(input())
result = []
for i in s:
    if s.count(i) >= k:
        result.append(i)
print("".join(i for i in result))