def printArrArr(arr):
    for i in arr:
        print(i)
    # print(len(arr), len(arr[0]))


def addSquare(arr):
    arr.insert(0, ['.'for _ in range(len(arr[0]))])
    arr.append(['.'for _ in range(len(arr[0]))])
    for i in arr:
        i.insert(0, '.')
        i.append('.')
    return arr


def numLive(arr, i, j):
    numL = 0
    for k in (-1, 0, 1):
        if arr[i+k][j-1] == '#':
            numL += 1
    for k in (-1, 1):
        if arr[i+k][j] == '#':
            numL += 1
    for k in (-1, 0, 1):
        if arr[i+k][j+1] == '#':
            numL += 1
    return numL


square = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '#', '#', '#', '#', '.', '.', '.', '.', '.'],
          ['.', '#', '#', '#', '#', '.', '.', '.', '.', '.'],
          ['.', '#', '#', '#', '#', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]


# printArrArr(square)
k = int(input())

for l in range(k):
    addSquare(square)
    rez = []

    for i in range(1, len(square)-1):
        rez.append([])
        for j in range(1, len(square[0])-1):
            nLive = numLive(square, i, j)
            if square[i][j] == '#':
                if nLive in (2, 3):
                    rez[i-1].append('#')
                else:
                    rez[i-1].append('.')
            else:
                if nLive == 3:
                    rez[i-1].append('#')
                else:
                    rez[i-1].append('.')
    print(l)
    printArrArr(rez)
    square = rez
# print()
# printArrArr(rez)
