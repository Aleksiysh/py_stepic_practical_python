x, y, length = 0, 0, 1
commands = list(input())
for command in commands:
    if command == 'l':
        x -= 1
    elif command == 'r':
        x += 1
    elif command == 'u':
        y += 1
    elif command == 'd':
        y -= 1
    elif command == '*':
        length += 1
    elif command == '#':
        length -= 1
    if length == 0:
        break

print(x,y)
print(length)
pass
