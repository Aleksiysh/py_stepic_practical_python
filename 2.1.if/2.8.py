x, y = int(input()), int(input())
if (x == 1 and y == 1 or 
        x == 1 and y == 8 or 
        x == 8 and y == 8 or 
        x == 8 and y == 8):
    print(3)
elif x == 1 or x == 8 or y == 1 or y == 8:
    print(5)
else:
    print(8)
