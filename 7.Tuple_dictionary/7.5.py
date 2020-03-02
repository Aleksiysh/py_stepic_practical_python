def dog_owners(pets):
    d = {}
    for rec in pets:
        onwer = tuple(rec[1::])
        d[onwer] = d.get(onwer, []) + [rec[0]]
    return d


def main():
    pets = [("Fido", "John", "Malkovic", 22),
            ("Butch", "Jake", "Smirnoff", 18),
            ("Zooma", "Simon", "Ng", 32),
            ("Chase", "Martha", "Black", 73),
            ("Rocky", "Simon", "Ng", 32)]
    print(dog_owners(pets))


if __name__ == '__main__':
    main()
