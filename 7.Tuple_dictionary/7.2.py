def vector_sum(v1, v2):
    v = []
    for i in range(len(v1)):
        v.append(v1[i]+v2[i])
    return tuple(v)


def main():
    v1 = (1, 2)
    v2 = (3, 4)
    print(vector_sum(v1, v2))


if __name__ == '__main__':
    main()
