s = input()
n = int(input())
a = s.count('a')
minimum_a = n // len(s)
find_a = s[:int((n%len(s)))].count('a')
print('result:%d'%((a * minimum_a )+ find_a))