def getLeft(src, spaces):
    pos = src  
    x = 0
    y = 0
    while (x < 2):
        if((pos%8 == 0)):
            break
        x += 1
        pos -= 1
    if(pos < 0):
        return
    if(x == 2):
        if((pos + 8) <= 63):
            spaces.append(pos + 8)
        if(0 <= (pos - 8)):
            spaces.append(pos - 8)



def getRight(src, spaces):
    pos = src  
    x = 0
    y = 0
    while (x < 2):
        if((pos%8 == 7)):
            break
        x += 1
        pos += 1
    if(pos > 63):
        return
    if(x == 2):
        if((pos + 8) <= 63):
            spaces.append(pos + 8)
        if(0 <= (pos - 8)):
            spaces.append(pos - 8)

def getUp(src, spaces):
    pos = src  
    x = 0
    y = 0
    while (x < 2):
        if((pos < 8)):
            break
        x += 1
        pos -= 8
    if(pos < 0):
        return
    if(x == 2):
        if((pos % 8) < 7):
            spaces.append(pos + 1)
        if((pos % 8) > 0):
            spaces.append(pos - 1)

def getDown(src, spaces):
    pos = src  
    x = 0
    y = 0
    while (x < 2):
        if((pos > 55)):
            break
        x += 1
        pos += 8
    if(pos > 63):
        return
    if(x == 2):
        if((pos % 8) < 7):
            spaces.append(pos + 1)
        if((pos % 8) > 0):
            spaces.append(pos - 1)

def bfs(spaces, dest):
    global count
    count += 1
    tempSpaces = []

    while spaces:
        temp = spaces.pop(0)
        getRight(temp, tempSpaces)
        getLeft(temp, tempSpaces)
        getUp(temp, tempSpaces)
        getDown(temp, tempSpaces)
    if (dest in tempSpaces):
        return
    spaces = tempSpaces
    bfs(spaces, dest)



def answer(src, dest):
    if(src == dest):
        return 0
    global count
    count = 0
    spaces = []
    spaces.append(src)
    bfs(spaces, dest)     
    return count

count = 0

