def calc(a, op, b):

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    ops = {'+': add,
           '-': sub,
           '*': mul,
           '/': div}
    return ops.get(op)(a, b)


def main():
    print(calc(2, '+', 4) == 6,
          calc(3, "/", 2) == 1.5,
          calc(3, '*', 13) == 39,
          calc(4, "-", 3) == 1)


if __name__ == '__main__':
    main()
