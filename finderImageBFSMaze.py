#? subtitle
# # == not allowed spaces
# " " == allowed spaces
# O == start point
# 0 == end point
# X == path

from array import array
import string
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


def findStart(convertedMaze:array):
    startPointX = 0
    startPointY = 0
    for countRow, row in enumerate(convertedMaze):
        for countColumn, column in enumerate(row):
            if column == "O":
                startPointX = countColumn
                startPointY = countRow
                return (startPointX, startPointY)


def NodeVisited(visited, newNode):
    solved = False
    for solvedNode in visited:
        if newNode == solvedNode:
            solved = True
    return solved


def findNeighbors(convertedMaze:array, vertex, visited):
    allowedMoves = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    neighbors = []
    for move in allowedMoves:
        neighborx = move[0] + vertex[0]
        neighbory = move[1] + vertex[1]
        if NodeVisited(visited, (neighborx, neighbory)):
            continue
        else:
            if convertedMaze[neighbory][neighborx] == " " or convertedMaze[neighbory][neighborx] == "0":
                    neighbors.append((neighborx, neighbory))

    return neighbors



def BackTrace(parents: dict, finalNode: tuple, startNode: tuple):
    path = [finalNode]
    while path[-1] != startNode:
        path.append(parents[path[-1]])
    return path


def solveMaze(convertedMaze:array):
    startTime = time()
    queue = []
    visited = []
    parents = {}
    start = (findStart(convertedMaze)[0], findStart(convertedMaze)[1])
    queue.append((start[0],start[1]))
    while queue:
        for neighbor in findNeighbors(convertedMaze, (queue[0][0], queue[0][1]), visited):
            parents[neighbor] = (queue[0][0], queue[0][1])
            if convertedMaze[neighbor[1]][neighbor[0]] == "0":
                end = time()
                for pos in reversed(BackTrace(parents, neighbor, start)):
                    convertedMaze[pos[1]][pos[0]] = "X"
                    print("=-"*10)
                    for row in convertedMaze:
                        print(f'{row}')
                    print("=-"*10)
                    sleep(0.2)
                print("Success")
                print(f"Time to solve: {end - startTime :.3f}s")

                return "sucess"
            queue.append((neighbor[0], neighbor[1]))
        
        visited.append((queue[0][0], queue[0][1]))
        queue.pop(0)
                
                
        # print("=-"*10)
        # for row in convertedMaze:
        #     print(f'{row}')
        # print("=-"*10)
        
        # sleep(0.1)

solveMaze(convertMaze(f'Mazes/Maze{maze}.jpg'))

