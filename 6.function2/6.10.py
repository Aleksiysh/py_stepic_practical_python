def header(head,mark = 1):
    if mark  <1:
        mark = 1
    if mark > 6:
        mark =6
    return '#'*mark +' ' + head


print(header('A',10))