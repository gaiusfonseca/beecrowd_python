#! /usr/bin/python
# calcula a média ponderada dadas duas notas
def average(score1, score2):
    wheight1 = 3.5
    wheight2 = 7.5

    result = (wheight1 * score1 + wheight2 * score2) / (wheight1 + wheight2)

    return result

a = round(float(input()), 1)
b = round(float(input()), 1)
wAverage = average(a, b)

print('MEDIA = {:.5f}'.format(wAverage))