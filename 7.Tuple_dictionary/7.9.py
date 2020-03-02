def fix_duplicates(ids):
    dict1 = {}
    rez = []
    for char in ids:
        if char in dict1:
            dict1[char] += 1
            rez.append(char + '_' + str(dict1[char]))
        else:
            dict1[char] = 0
            rez.append(char)
    return rez




def main():
    ids = ["a", "b", "c", "a", "a", "d", "c"]
    print(fix_duplicates(ids))


if __name__ == '__main__':
    main()