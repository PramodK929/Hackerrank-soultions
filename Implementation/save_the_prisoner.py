def saveThePrisoner(n, m, s):
    # Complete this function
    t = (s+(m-1))%n
    if t is 0:return n
    return t
t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
