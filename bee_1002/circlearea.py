#! /usr/bin/python
# calcula a área do círculo

pi = 3.14159
r = float(input())

area = round(pi * r ** 2, 4)

print('A={0:.4f}'.format(area))