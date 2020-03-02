sum_sqr = 0
while True:
    str = input()
    if str == '.':
        break
    sum_sqr += float(str)**2
print(sum_sqr)
