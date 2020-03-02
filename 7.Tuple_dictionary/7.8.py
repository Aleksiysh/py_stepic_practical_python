def average_attempts(attempts, names):
    rez = {}
    for name in names:
        for attempt in attempts:
            if attempt[0] == name[0]:
                if name[1] in rez:
                    rez[name[1]][0] += 1
                    rez[name[1]][1] += attempt[2]
                else:
                    rez[name[1]] = [1, attempt[2]]
    for k in rez:
        rez[k] = rez[k][1]/rez[k][0]
    return rez


def main():
    attempts = [(1232323323415, 1, 43),
                (1232323323415, 2, 3),
                (114349, 1, 0)
                ]
    names = [(114349, "Arkady"),
             (1232323323415, "Random")]
    print(average_attempts(attempts, names))


if __name__ == '__main__':
    main()