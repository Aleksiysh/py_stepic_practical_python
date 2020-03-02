def func(l):
    l1 = []
    for i in l:
        if i in l1:
            continue
        else:
            l1.append(i)
    return l1


def f1(l):
    return list(set(l))


print(f1([1, 2, 2, 3, 4, 3, 6, 2]))
