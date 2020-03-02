def concat(*strs, sep = ' '):
    return sep.join(strs)


print(concat('a','b',sep = ':'))