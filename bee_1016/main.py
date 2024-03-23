#! /usr/bin/python

# calcula o tempo necessário em minutos para produzir um afastamento 
# ente dois veículos que se deslocam na mesma direção

def estimateTime(distance):
    ratio = (90 - 60) / 60
    return distance / ratio
    
distance = int(input())
message = '{:.0f} minutos'.format(estimateTime(distance))

print(message)
