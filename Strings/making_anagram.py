f = input()
s = input()
count = 0
alphabatic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
for i in alphabatic:
    count+=abs(f.count(i)-s.count(i))
print(count)