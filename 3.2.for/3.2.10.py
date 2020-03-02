rez = []
while True:
    str = input()
    if str == '.':
        break
    rez.append(int(str))
k = 0
for i in range(len(rez)):
    if rez[i] < 3:
        rez.insert(k, rez.pop(i))
        k += 1
print(rez)
