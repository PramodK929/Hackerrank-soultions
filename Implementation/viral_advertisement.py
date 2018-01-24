n = int(input())
people = 5
result = 0
for i in range(0, n):
    people = int(people/2)
    result += people
    people *= 3
print(result)