s = 100000
p = 10
n = int(input())
for i in range(n):
    s += s*p/100
print(int(s))
pass
