
inStr = list(input())
outStr = []

print(inStr)
for i in range(len(inStr)):
    if i == 0:
        outStr.append(inStr[i+1])
    elif i in range(1,len(inStr)-1):
        nLive = ((inStr[i-1] == '#') + (inStr[i+1]=='#'))
        if inStr=='#' and  nLive in (0,2):
                outStr.append('.')
        elif nLive==1:        
            outStr.append('#')
        else:
            outStr.append(inStr[i])
    else:
        outStr.append(inStr[i-1])


print(outStr)
