def code_number(num):
    line = ''
    description = { 1: "one",
                    2: "two",
                    3: "three",
                    4: "four",
                    5: "five",
                    6: "six",
                    7: "seven",
                    8: "eight",
                    9: "nine",
                    0: "zero"}
    for n in str(num):
        line+=( description[int(n)]+' ')
    return line[:-1]


def main():
    print(code_number(int(input())))





if __name__ == '__main__':
    main()
