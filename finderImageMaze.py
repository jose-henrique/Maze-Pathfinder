#? subtitle
# 0 == # == not allowed spaces
# 1 == " " == allowed spaces
# 2 == "O" == start point
# 3 == "0" == end point
# 4 == "X" == path

from time import sleep, time
from PIL import Image


maze = int((input("What maze, do you like that I solve? (only numbers)")))

def convertMaze(PathImage):
    image = Image.open(PathImage)
    imageConverted = image.convert("RGB")
    width, height = image.size


    convertedMaze = []
    count = 0
    for row in range(0, height):
        convertedMaze.append([])
        for column in range(0, width):
            color = imageConverted.getpixel((column, row))
            if color[0] <= 10 and color[1] <= 10 and color[2]<= 10:
                convertedMaze[count].append(0)
            elif color[0] >= 250 and color[1] >= 250 and color[2]>= 250:
                convertedMaze[count].append(1)
            elif color[0] <= 5 and color[1] >= 250 and color[2]<= 5:
                convertedMaze[count].append(2)
            elif color[0] <= 5 and color[1] <= 5 and color[2] >= 250:
                convertedMaze[count].append(3)
        count += 1
    return convertedMaze


def findStart(convertedMaze):
    countRow = 0
    startPointX = 0
    startPointY = 0
    for row in convertedMaze:
        countColumn = 0
        for column in row:
            if column == 2:
                startPointX = countColumn
                startPointY = countRow
                return (startPointX, startPointY)
            countColumn +=1
        countRow +=1

def SolveMaze(convertedMaze, PathImage):
    start = time()
    allowedMoves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    currentPointX = findStart(convertedMaze)[0]
    currentPointY = findStart(convertedMaze)[1]
    sucess = 0
    while sucess != 1:
        for move in allowedMoves:
            nextMoveImpossibility = 0
            newx = move[0] + currentPointX
            newy = move[1] + currentPointY
            if convertedMaze[newy][newx] == 3:
                sucess = 1
                convertedMaze[newy][newx] = 4
                print("=-"*10)
                for row in convertedMaze:
                    print(f'{row}')
                print("=-"*10)
                print("SUCESS")
                
            elif convertedMaze[newy][newx] == 1:
                convertedMaze[newy][newx] = 4
                currentPointX = newx
                currentPointY = newy

                for predictMove in allowedMoves:
                    predictX = currentPointX + predictMove[0]
                    predictY = currentPointY + predictMove[1]

                    if convertedMaze[predictY][predictX] == 0 or convertedMaze[predictY][predictX] == 4:
                        nextMoveImpossibility += 1
                
                    if nextMoveImpossibility == 4:
                        convertedMaze = convertMaze(PathImage)
                        currentPointX = findStart(convertedMaze)[0]
                        currentPointY = findStart(convertedMaze)[1]

        
        # print("=-"*10)
        # for row in convertedMaze:
        #     print(f'{row}')
        # print("=-"*10)
        #sleep(0.7)
    end = time()
    print(f'Time to solve: {end - start :.2f} s!')


SolveMaze(convertMaze(f'Mazes/Maze{maze}.jpg'), f'Mazes/Maze{maze}.jpg')