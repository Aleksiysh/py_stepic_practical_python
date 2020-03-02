x, y, z = [int(input()) for _ in '123']

# if x < y and y < z and x < z:
#     print(x, y, z, sep='\n')
# elif x < y and x < z and z < y:
#     print(x, z, y, sep='\n')
# elif y < z and y < x and x < z:
#     print(y, x, z, sep='\n')
# elif y < z and y < z and z < x:
#     print(y, z, x, sep='\n')
# elif z < x and z < y and x < y:
#     print(z, x, y, sep='\n')
# else:
#     print(z, y, x, sep='\n')

if x == min(x, y, z):
    print(x)
    print(min(y, z))
    print(max(y, z))
elif y == min(x, y, z):
    print(y)
    print(min(x, z))
    print(max(x, z))
else:
    print(z)
    print(min(x, y))
    print(max(x, y))
