n = int(input())
B = input()
change = 0
secondary_string = ""
count = 0
for i in range(0, n - 2):
    if B[i] == '0' and B[i + 1] == '1' and B[i + 2] == '0':
        if count>0:
            if  secondary_string[i] == '0' and secondary_string[i+1] == '1' and secondary_string[i+2] == '0':
                secondary_string +=secondary_string[i]+secondary_string[i+1]+'1'
                change+=1
        else:
            secondary_string += B[i]+B[i+1]+'1'
            change += 1
print(0 if change==0 else change-1)
