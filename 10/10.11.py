# [print(i) for i in range(10) if i % 2 == 0]
# print(all(range(10)))
# for i in range(2, 10):
#     a = all([i % x != 0 for x in range(2, i)])
#     print(i, a)
# pass

[print(i, end=' ')
 for i in range(2, 1000) if all([i % x != 0 for x in range(2, i)])]
