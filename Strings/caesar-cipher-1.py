n = int(input().strip())
s = input().strip()
k = int(input().strip())
r = []
cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in s[:]:
    if i in cap:
        r.append(chr(((cap.index(i)+ k) % 26)+65))
    elif i in small:
        r.append(chr(((small.index(i) + k) % 26) + 97))
    else:
        r.append(i)
print("".join(r))