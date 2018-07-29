
import random

def setup():
    size(600, 600)
    background(0, 0, 0)
    global numGrid, numList,newNumComb, endGame
    endGame = False 
    newNumComb = []
    numList = [2,2,4,2]

    numGrid = [[2, 0, 0, 0],
               [0, 2, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
    print(newNumComb)
    print(combineRightRow(numList))

    fill(255,255,255)
    textSize(100)
    text("2048", 0,90)
    
    textSize(20)
    text("Ciara, Monique, Alexis, Brianna", 0, 590)
def draw():
    global numGrid
    drawSquaresRow(numGrid[0] , 100)
    drawSquaresRow(numGrid[1] , 200)
    drawSquaresRow(numGrid[2] , 300)
    drawSquaresRow(numGrid[3] , 400)
    if endGame == True:
        background(0, 0, 0)
        fill(255, 255, 255)
        textSize(60)
        textAlign(CENTER)
        text("LOSER!", 300, 300)
        


def drawSquaresRow(numList, y):
    for index in range(0,4,1):
        fill(237, 232, 142)
        x = (index + 1) * 100 
        num = numList[index]
        rect(x, y, 90, 90)
        fill(0, 0, 0)
        textSize(35)
        textAlign(CENTER);
        if num == 0:
            num==None
        else:
            text(num, x + 35, y + 60)
            
#shifts one row to the left            
def shiftLeftRow(numList):
    newNumlist = []
    #group nums to left
    for index in range(0, 4, 1):
        currentNum = numList[index]
        if (currentNum == 0):
            currentNum = None 
        else:
            newNumlist.append(currentNum)
    #Add zeroes
    zerosAdd = 4 - len(newNumlist)
    zerolist = [0]*zerosAdd
    
    return newNumlist + zerolist

#shifts grid to the left 
def shiftLeftGrid(numGrid):
    newNumGrid = [] 
    #taking one of the rows in the grid and giving a new row to put in our grid 
    for i in range(0, 4, 1):
        newList = shiftLeftRow(numGrid[i]) 
        newNumGrid.append(newList)
    return newNumGrid

#Combines numbers towards the left in a row
def combineLeftRow(numList):
    global newNumComb
    newNumComb = []
    p = 0
    while p < 3:
        firstNum = numList[p]
        secondNum = numList[p +1]
        if firstNum == secondNum:
            sum = firstNum + secondNum
            newNumComb.append(sum)
            p = p + 2
        else: 
            p = p + 1
            newNumComb.append(firstNum)
    if p == 3:
        newNumComb.append(numList[3])
    # print(p)
    # print(sum)
    
    zerosAdd = 4 - len(newNumComb)
    zerolist = [0]*zerosAdd
    return newNumComb + zerolist

#Combines numbers towards the left in the grid
def combineLeftGrid(numGrid):
    newNumGrid = [] 
    #taking one of the rows in the grid and giving a new row to put in our grid 
    for i in range(0, 4, 1):
        newList = combineLeftRow(numGrid[i]) 
        newNumGrid.append(newList)
    return newNumGrid

#shifts one row to the right 
def shiftRightRow(numGrid):
    newNumlist = []
    #group nums to right
    for index in range(0, 4, 1):
        currentNum = numGrid[index]
        if (currentNum == 0):
            currentNum = None 
        else:
            newNumlist.append(currentNum)
    #Add zeroes
    zerosAdd = 4 - len(newNumlist)
    zerolist = [0]*zerosAdd
    
    return zerolist + newNumlist

#moves grid to the right
def shiftRightGrid(numGrid):
    newNumGrid = [] 
    #taking one of the rows in the grid and giving a new row to put in our grid 
    for i in range(0, 4, 1):
        newList = shiftRightRow(numGrid[i]) 
        newNumGrid.append(newList)
    return newNumGrid 

#combines rows towards the right
def combineRightRow(numList):
    global newNumComb
    newNumComb = []
    p = 3
    while p > 0:
        firstNum = numList[p]
        secondNum = numList[p -1]
        if firstNum == secondNum:
            sum = firstNum + secondNum
            newNumComb.append(sum)
            p = p - 2
        else: 
            p = p - 1
            newNumComb.append(firstNum)
    if p == 0:
        newNumComb.append(numList[0])

    zerosAdd = 4 - len(newNumComb)
    zerolist = [0]*zerosAdd
    #reverses the list 
    newNumComb.reverse()
    return zerolist + newNumComb

#Combines the grid going to the right
def combineRightGrid(numGrid):
    newNumGrid = [] 
    #taking one of the rows in the grid and giving a new row to put in our grid 
    for i in range(0, 4, 1):
        newList = combineRightRow(numGrid[i]) 
        newNumGrid.append(newList)
    return newNumGrid

#Taking numbers out of a specific row and column 
def takeOut(numGrid, colNum):
    newColList = []
    for rowNum in range(0, 4, 1):
        num = numGrid[rowNum][colNum]
        newColList.append(num)
    return newColList

#Putting back numbers out of a specific row and column 
def putBack(numGrid, newCol, columnNum):
    for row in range(0, 4, 1):
        numGrid[row][columnNum]= newCol[row]        
    print(numGrid)

#Moves the grid down        
def moveDown(numGrid):
    for columnNum in range(0, 4, 1):
        column = takeOut(numGrid, columnNum)
        column = shiftRightRow(column)
        column = combineRightRow(column)
        putBack(numGrid, column, columnNum)
        
#moves the grid up
def moveUp(numGrid):
    for columnNum in range(0, 4, 1):
        column = takeOut(numGrid, columnNum)
        column = shiftLeftRow(column)
        column = combineLeftRow(column)
        putBack(numGrid, column, columnNum)
                
def keyPressed():
    global numGrid
    global endGame
    oldGrid = numGrid
    if key == CODED:
        if keyCode == LEFT:
            numGrid = shiftLeftGrid(numGrid)
            numGrid = combineLeftGrid(numGrid)
        
        if keyCode == RIGHT:
            numGrid = shiftRightGrid(numGrid)
            numGrid = combineRightGrid(numGrid)
        if keyCode == UP:
            moveUp(numGrid)
        if keyCode == DOWN:
            moveDown(numGrid)
        if oldGrid == numGrid:
            print("No!")
        listOfEmptyBoxes = getEmptyCo(numGrid)
        emptyCount = len(listOfEmptyBoxes)
        if emptyCount == 0:
            endGame = True
            print("End Game")
        else:
            addNum(numGrid)
    

    
#adding numbers
def addNum(numGrid):
    emptyCo = getEmptyCo(numGrid)
    coordinate = random.choice(emptyCo)
    print(coordinate)
    addRowPosition = coordinate[0]
    addColPosition = coordinate[1]
    numGrid[addRowPosition][addColPosition] = random.randint(1,2) * 2
    
def getEmptyCo(numGrid):
    global numList
    emptyCo = []
    for row in range(0, 4, 1):
        for col in range(0, 4, 1):
            if numGrid[row][col] == 0:
                emptyCo.append([row,col])
    return emptyCo





          
