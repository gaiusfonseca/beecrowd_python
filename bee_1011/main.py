#! /usr/bin/python
# calcula o volume de uma esfera
import math

def sphereVolume(radius):
    pi = round(math.pi, 5)
    return 4 / 3 * pi * radius ** 3

radius = float(input())

print('VOLUME = {:.3f}'.format(sphereVolume(radius)))