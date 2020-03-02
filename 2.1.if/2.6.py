x = int(input())
if (x % 100 in range(10, 20)) or (x % 10 in range(5, 10)) or (x % 10 == 0):
    print(x, 'studentov')
elif x % 10 == 1:
    print(x, 'student')
else:
    print(x, 'studenta')
