d, m, y = input().split(' ')
ed, em, ey = input().split(' ')
if d < ed and m < em and y < ey:print(0)
elif y > ey :print(10000)
else:
    month = int(int(m) - int(em))
    day = int(int(d) - int(ed))
    fine1 = 0
    fine2 = 0
    if month > 0:fine1 = month * 500
    if day > 0:fine2 = day * 15
    print(fine1 + fine2)