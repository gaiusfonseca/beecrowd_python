#! /usr/bin/python

# seleciona o maior dentre dois valores
def maximum(valueA, valueB):
    return (valueA + valueB + abs(valueA - valueB)) / 2

# segmenta o array em grupos de valores tomados dois a dois
def maximumInArray(values):

    if len(values) > 1:                                 # se o array for maior do que 1
        values[0] = maximum(values[0], values[1])       # captura o maior entre os dois primeiros elementos
        del values[1]                                   # elimina o segundo elemento
        maximumInArray(values)                             # repete recursivamente até que só haja um elemento
    
    return values[0]                                    # quando finalmente tiver apennas um elemento (o maior), retorna

# captura as entradas e as retorna como um array de ints
def getValues():
    values = input().split()

    for i in range(len(values)):
        values[i] = int(values[i])
    
    return values


values = getValues()
message = '{maior:.0f} eh o maior'
print(message.format(maior = maximumInArray(values)))