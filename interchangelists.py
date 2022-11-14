def swapList(newList):

    newList[0],newList[-1] = newList[-1],newList[0]
    return newList

newList = [24,112,44,667,888,22]
print(swapList(newList))



#output = [22,112,44,667,888,24]
