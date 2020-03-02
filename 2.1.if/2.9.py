x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if (abs(x1-x2) > 1 or abs(y1-y2) > 1
        or (x1 == x2 and y1 == y2)
        or not(x1 in range(1, 9))
        or not(x2 in range(1, 9))
        or not(y1 in range(1, 9))
        or not(y2 in range(1, 9))):
    print('NO')
else:
    print('YES')
