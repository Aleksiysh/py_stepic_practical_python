x, y = float(input()), float(input())

if y > 0:
    if x > 0:
        rez = 1
    else:
        rez = 2
else:
    if x > 0:
        rez = 4
    else:
        rez = 3
print(rez)
