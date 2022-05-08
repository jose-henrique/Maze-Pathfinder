#? subtitle
# # == not allowed spaces
# " " == allowed spaces
# O == start point
# 0 == end point
# X == path

from time import  time, sleep
from PIL import Image
from random import randint


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
                convertedMaze[count].append("#")
            elif color[0] >= 250 and color[1] >= 250 and color[2]>= 250:
                convertedMaze[count].append(" ")
            elif color[0] <= 5 and color[1] >= 250 and color[2]<= 5:
                convertedMaze[count].append("O")
            elif color[0] <= 5 and color[1] <= 5 and color[2] >= 250:
                convertedMaze[count].append("0")
        count += 1
    return convertedMaze


def findStart(convertedMaze):
    startPointX = 0
    startPointY = 0
    for countRow, row in enumerate(convertedMaze):
        for countColumn, column in enumerate(row):
            if column == "O":
                startPointX = countColumn
                startPointY = countRow
                return (startPointX, startPointY)

def SolveMaze(convertedMaze, PathImage):
    start = time()
    allowedMoves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    currentPointX = findStart(convertedMaze)[0]
    currentPointY = findStart(convertedMaze)[1]
    sucess = 0
    while sucess != 1:
        moveIndex = randint(0, len(allowedMoves)-1)
        move = allowedMoves[moveIndex]
        nextMoveImpossibility = 0
        newx = move[0] + currentPointX
        newy = move[1] + currentPointY
        if convertedMaze[newy][newx] == "0":
            sucess = 1
            convertedMaze[newy][newx] = "X"
            print("=-"*10)
            for row in convertedMaze:
                print(f'{row}')
            print("=-"*10)
            print("SUCESS")
                
        elif convertedMaze[newy][newx] == " ":
            convertedMaze[newy][newx] = "X"
            currentPointX = newx
            currentPointY = newy

            for predictMove in allowedMoves:
                predictX = currentPointX + predictMove[0]
                predictY = currentPointY + predictMove[1]

                if convertedMaze[predictY][predictX] == "#" or convertedMaze[predictY][predictX] == "X":
                    nextMoveImpossibility += 1
                
            if nextMoveImpossibility == 4:
                convertedMaze = convertMaze(PathImage)
                currentPointX = findStart(convertedMaze)[0]
                currentPointY = findStart(convertedMaze)[1]

        
        # print("=-"*10)
        # for row in convertedMaze:
        #     print(f'{row}')
        # print("=-"*10)
        # sleep(0.3)
    end = time()
    print(f'Time to solve: {end - start :.2f} s!')


SolveMaze(convertMaze(f'Mazes/Maze{maze}.jpg'), f'Mazes/Maze{maze}.jpg')