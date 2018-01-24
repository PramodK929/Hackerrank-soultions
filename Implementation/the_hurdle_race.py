n, k = input().split(' ')
hurdle = [int(i) for i in input().split(' ')]
if max(hurdle)-int(k)>0: print(max(hurdle)-int(k))
else:print(0)