
max_number, max_prev = float(input()), float(input())
max_number, max_prev = max(max_number, max_prev), min(max_number, max_prev)

while True:
    str = input()
    if str == '.':
        break
    f_str = float(str)
    if f_str > max_prev and f_str < max_number:
        max_prev = f_str
    if f_str > max_prev and f_str > max_number:
        max_prev = max_number
        max_number = f_str
print(max_prev)
