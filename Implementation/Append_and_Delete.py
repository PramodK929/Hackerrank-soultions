first = input()
second = input()
k = int(input())
result = []
p = int(min(len(first), len(second)))-1
for i in range(0, p):
    if first[int(i)] is second[int(i)]:
        result.append(first[i])
    else:
        break
ref = ''.join(result)
if len(first)>=len(second):
    num = (len(first) - len(ref)) + (len(second) - len(ref))
    if first == second and k % 2 == 0:
        print("Yes")
    elif k>=int(num):
        print("Yes")
    else :
        print("No")
else:
    num2 =2 * ((len(second) - len(ref)) - (len(first) - len(ref)))
    if num2 >= k and num2%k != 0:
        print('No')
    else:
        last_ref = k % int(num2)
        if len(ref)<1:
            print('No')
        elif int(last_ref) % int(len(ref)) == 0:
            print('Yes')
        else:
            print('No')