
max_number = float(input())
while True:
    str = input()
    if str == '.':
        break
    if max_number < float(str):
        max_number = float(str)
print(max_number)
