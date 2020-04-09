def line_count(filename):
    count = 0
    with open(filename) as f:
        while(f.readline()):
            count += 1
    return count


def char_count(filename):
    return len(open(filename).read())


def sum_numbers(filename):
    return sum(map(int, open(filename).readlines()))


def write_message(filename, message):
    with open(filename, 'w') as f:
        f.write(message)


def log(filename, message):
    with open(filename, 'a') as f:
        f.write(message + '\n')


def total_sum(filename):
    with open(filename) as f:
        return sum(map(float, f.read().split()))


def minmax_coords(filename):
    with open(filename) as f:
        lst = [list(map(int, x.split())) for x in f.readlines()]
    if not lst:
        return None, None, None, None
    firsts = [x[0] for x in lst if x]
    seconds = [x[1] for x in lst if x]
    return min(firsts), max(firsts), min(seconds), max(seconds)


def solved_tasks1(filename):
    st = {}
    with open(filename) as file:
        for line in file:
            if len(line) > 1:
                stud_id, task = line.split(',')
                stud_id = int(stud_id)
                task = int(task)
                if stud_id not in st:
                    st[stud_id] = 0
                st[stud_id] += 1
    return st


def solved_tasks(filename):
    st = {}
    with open(filename) as file:
        for line in file:
            if len(line) > 1:
                stud_id, task = line.split(',')
                stud_id = int(stud_id)
                task = int(task)
                if stud_id not in st:
                    st[stud_id] = set()
                st[stud_id].add(task)
    rez = {}
    for x in st:
        rez[x] = len(st[x])
    return rez


def mean_petal(filename, variety):
    with open(filename) as f:
        f.readline()
        dct = {}
        for line in f.readlines():
            a = line.strip().split(',')
            lst = list(map(float, a[:-1]))
            key = a[4][1:-1]
            if key not in dct:
                dct[key] = []
            dct[key].append(lst)
    return sum([x[2] for x in dct[variety]])/len(dct[variety])


filename = 'd:\\py\\11\\file.txt'
print(mean_petal(filename, 'Setosa'))
