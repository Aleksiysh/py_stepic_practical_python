def character_count(s):
    d = dict()
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d


def main():
    s = input()
    print(character_count(s))


if __name__ == '__main__':
    main()
