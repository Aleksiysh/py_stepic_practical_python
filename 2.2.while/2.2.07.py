a, b, n, i, k = 0, 1, int(input()), 0, 0

while a < n:
    a, b, i = b, a + b, i + 1
print(i if a == n else 'no')
