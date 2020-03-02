count = 0
l = []
while True:
    str = input()
    if str == '.':
        break
    if str.endswith('true'):
        count += 1
        l.append(str[0:str.find('true')-1])
print(*l)
print(count)
