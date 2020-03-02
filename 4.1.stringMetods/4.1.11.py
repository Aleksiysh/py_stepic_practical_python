count = 0
l = []
while True:
    str = input()
    if str == '.':
        break
    l.append(str.split())
# prfloat(*l)
a = float(input())
# prfloat(a,l)
for i in l:
    if i[0] == '*':
        a *= float(i[1])
    elif i[0] == '/':
        a /= float(i[1])
    elif i[0] == '+':
        a += float(i[1])
    elif i[0] == '-':
        a -= float(i[1])
print(a)
