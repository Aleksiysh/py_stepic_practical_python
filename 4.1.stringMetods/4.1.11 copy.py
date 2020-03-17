
def foo(a, line):

    ops = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b
           }
    return ops[line[0]](a, float(line[1]))


def main():
    l = []
    while True:
        str = input()
        if str == '.':
            break
        l.append(str.split())
    a = float(input())
    for i in l:
        a = foo(a, i)
    print(a)


if __name__ == '__main__':
    main()
