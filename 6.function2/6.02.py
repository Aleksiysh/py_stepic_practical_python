def number_of_frogs(year):
    if year == 1:
        return 120

    return 2*(number_of_frogs(year-1)-50)

    pass


print(number_of_frogs(10))