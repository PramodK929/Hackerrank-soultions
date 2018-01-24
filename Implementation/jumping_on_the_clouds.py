n = int(input())
clouds = [int(i) for i in input().split(' ')]
jump= 0
k = 0
while k < n-3:
    num1 = n + 2
    num2 = n + 1
    if clouds[k]!=1:
        k = num1
        jump+=1
    else:
        k = num2
        jump+=1
if k < n-1:
    jump+=1
print(jump)