def printTable(table):
    lengthList = []
    for i in range(len(table)):
        maxLength = 0
        for j in range(len(table[i])):
            if(maxLength < len(table[i][j])):
                maxLength = len(table[i][j])
        lengthList.append(maxLength)
    for i in range (len(table[i])):
        for j in range(len(table)):
            print(table[j][i].rjust(lengthList[j]) + " ", end="")
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)