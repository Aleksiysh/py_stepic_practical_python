sum, n = 0, 0
while True:
    str = input()
    if str == '.':
        break
    if not(n % 2):
        sum += float(str)
    n += 1
print(sum)
