def update_age(owners, owner, new_age):
    if owner in owners:
        new_key = tuple(list(owner)[:2] + [new_age])
        owners[new_key] = owners.pop(owner)
    return owners


def main():
    dog_owners = {("John", "Malkovic", 22): ["Fido"],
                  ("Jake", "Smirnoff", 18): ["Butch"],
                  ("Simon", "Ng", 32): ["Zooma", "Rocky"],
                  ("Martha", "Black", 73): ["Chase"]
                  }
    update_age(dog_owners, ("Jake", "Smirnoff", 18), 22)
    print(dog_owners[("Jake", "Smirnoff", 22)] == ['Butch'])


if __name__ == '__main__':
    main()
