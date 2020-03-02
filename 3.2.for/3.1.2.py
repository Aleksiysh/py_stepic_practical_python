rez, i, i_max = [], 0, 0
while True:
    str = input()
    if str == '.':
        break
    rez.append(int(str))
    if rez[i] > rez[i_max]:
        i_max = i
    i += 1
rez.insert(0, rez.pop(i_max))
print(rez)
