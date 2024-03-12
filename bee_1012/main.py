#! /usr/bin/python
import math

# calcula a área do triângulo
def triangleArea(base, height):
    return base * height / 2.0

# calcula a área do círculo
def circleArea(radius):
    pi = round(math.pi, 5)
    return pi * radius ** 2

# calcula a área do trapézio
def trapeziumArea(minorBase, majorBase, height):
    return (minorBase + majorBase) * height / 2.0

# calcula a área do quadrado
def squareArea(side):
    return side ** 2

# calcula a área do retângulo
def rectangleArea(base, height):
    return base * height

# exibe a área do triângulo
def printTriangleArea(values):
    base = values[0]
    height = values[2]
    print('TRIANGULO: {:.3f}'.format(triangleArea(base, height)))

# exibe a área do círculo
def printCircleArea(values):
    radius = values[2]
    print('CIRCULO: {:.3f}'.format(circleArea(radius)))

# exibe a área do trapézio
def printTrapeziumArea(values):
    minorBase, majorBase, height = values
    print('TRAPEZIO: {:.3f}'.format(trapeziumArea(minorBase, majorBase, height)))

# exibe a área do quadrado
def printSquareArea(values):
    side = values[1]
    print('QUADRADO: {:.3f}'.format(squareArea(side)))

# exibe a área do retângulo
def printRectangleArea(values):
    base = values[0]
    height = values[1]
    print('RETANGULO: {:.3f}'.format(rectangleArea(base, height)))

# inínico do main
values = input().split()

# recebendo o input e convertendo em valores float de precisão 1
for i in range(len(values)):
    values[i] = round(float(values[i]), 2)

printTriangleArea(values)
printCircleArea(values)
printTrapeziumArea(values)
printSquareArea(values)
printRectangleArea(values)