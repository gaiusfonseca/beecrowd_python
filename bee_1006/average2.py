#! /usr/bin/python
# calcula a media ponderada a partir de tres diferentes notas

def wAverage(scores):
    wheigts = [2, 3, 5]
    
    totalWheigt = sumRange(wheigts)
    result = sumProduct(scores, wheigts)
    
    return result / totalWheigt

def sumRange(array):
    total = 0

    for i in range(len(array)):
        total += array[i]
    
    return total

def sumProduct(array1, array2):
    product = 0

    for i in range(len(array1)):
        product += array1[i] * array2[i]
    
    return product

scores = [0] * 3

for i in range(3):
    scores[i] = round(float(input()), 1)

print('MEDIA = {:.1f}'.format(wAverage(scores)))