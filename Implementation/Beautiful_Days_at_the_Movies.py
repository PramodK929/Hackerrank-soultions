def rev(Number):
    Reverse = 0
    while Number > 0:
        Reminder = Number % 10
        Reverse = (Reverse * 10) + Reminder
        Number = Number // 10
    return Reverse
i, j, k = input().split(' ')
count = 0
for p in range(int(i), int(j)):
    if abs(int(p) - int(rev(p))) % int(k) == 0:
        count += 1
print(count)