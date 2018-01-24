n = int(input().strip())
a = []
x = []
for i in range(n):
   ip = str(input().strip())
   v = str(ip)
   result = []
   for e in v:
       if e is not '9':
           result.append(e)
       else:
           result.append('x')
   x.append("".join(result))
for i in x:
    print(i)
