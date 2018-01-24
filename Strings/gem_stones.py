def gemstones(arr):
    # Complete this function
    a = "".join(arr)
    b = []
    result = False
    for i in range(0, len(a)):
        if a[i] not in b:
            b.append(a[i])
    count=0
    for ele in b:
        for j in arr:
            if ele in j:
                result = True
            else:
                result = False
                break
        if result == True:
            count+=1
    return count
n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)