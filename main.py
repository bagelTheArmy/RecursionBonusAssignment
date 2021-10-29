def addormultiply(string):
    if "*" in string:
        x = string.split("*")
        return int(x[1]) * int(x[0])
    if "+" in string:
        x = string.split("+")
        return int(x[1]) + int(x[0])

def parenthesisChecker(string):
    startpos = 0
    endChecking = False
    for i in range(0,len(string)):
        if string[i] == "(" and not endChecking:
            startpos = i
        if string[i] == ")" and not endChecking:
            endpos = i
            endChecking = True
    if(string.isnumeric()):
        return string
    elif(endChecking):
        x = string.replace(string[startpos:endpos + 1], str(addormultiply(string[startpos + 1:endpos])))
        return parenthesisChecker(x)
    else:
        return addormultiply(string)


dontLeave = True
while(dontLeave):
    x = input('input a string')
    if(x == ""):
        dontLeave = False
    else:
        num = parenthesisChecker(x)
        print(num)


