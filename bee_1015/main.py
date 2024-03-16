#! /usr/bin/python

import math

# retorna um array contendo dois valores float que representam os pontos x e y de um ponto
def getPoint():
    point = input().split()

    for i in range(len(point)):
        point[i] = float(point[i])

    return point

def getDistance(pointA, pointB):
    x = 0
    y = 1
    
    xDistance = (pointB[x] - pointA[x]) ** 2
    yDistance = (pointB[y] - pointA[y]) ** 2
    
    return math.sqrt(xDistance + yDistance)

pointA = getPoint()
pointB = getPoint()
message = '{distance:.4f}'

print(message.format(distance = getDistance(pointA, pointB)))