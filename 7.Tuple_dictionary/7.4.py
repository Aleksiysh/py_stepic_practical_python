def max_par(a, b, c):
    if a > 0:
        return None
    x = -b / (2 * a)
    y = a*x*x+b*x+c
    return (x, y)


def main():
    a, b, c = tuple(map(float, input().split(' ')))
    print(max_par(a, b, c))


if __name__ == '__main__':
    main()
