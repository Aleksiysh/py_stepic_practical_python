n, sum = 0, 0
while True:
    str = input()
    if str == '.':
        break
    sum += int(str)
    n += 1
print(sum/n)
