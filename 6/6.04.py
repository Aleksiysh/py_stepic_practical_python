def paths_count(x, y):    
    if x > 0 and y > 0:
        return paths_count(x - 1, y)+paths_count(x, y - 1)
    elif x > 0 or y > 0:
        return 1
    # else:
    #     return 0


print(paths_count(int(input()),int(input())))