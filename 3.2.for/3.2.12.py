
inStr = list(input())
outStr = []

print(inStr)
for i in range(len(inStr)):
    if i == 0:
        outStr.append(inStr[i+1])
    elif i in range(1,len(inStr)-1):
        nLive = ((inStr[i-1] == '#') + (inStr[i+1]=='#'))
        if nLive==1:
                outStr.append('#')
        elif nLive==2:        
            outStr.append('.' if inStr[i]=='#' else '#')
        else:
            outStr.append('.')
    else:
        outStr.append(inStr[i-1])


print(outStr)
