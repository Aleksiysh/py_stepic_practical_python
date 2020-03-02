def sq_sum(*numbers):
    s = 0.
    for n in numbers:
        s+=n*n
    return s



print(sq_sum(1,2,2,4))