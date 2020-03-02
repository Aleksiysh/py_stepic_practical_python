s = 100000
p = 10
n = int(input())
for _ in range(n*12):
    s += s * p / 100 / 12
print(int(s))
pass
