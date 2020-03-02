def is_prime(a):
    k, i = a, 2
    if a <= 1:
        return False
    while i < int(k**0.5)+1:
        if not (k % i):
            return False
        i += 1
    return True

while 1:
    print(is_prime(int(input())))
