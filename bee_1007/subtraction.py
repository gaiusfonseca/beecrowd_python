#! /usr/bin/python
# lê quatro valores e calcula a diferença entre seus produtos

def subtractProduct(values):
    a, b, c, d = values
    return a * b - c * d

values = [0] * 4

for i in range(4):
    values[i] = int(input())

print('DIFERENCA = {}'.format(subtractProduct(values)))