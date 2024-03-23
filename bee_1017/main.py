#! /usr/bin/python

# calcula quantos litros de combustível seriam necessários para 
# realizar uma viagem considerando-se um rendimento e velocidade média

def estimateFuel(time, speed): 
    return time * speed / 12

time = int(input())
speed = int(input())
fuel = estimateFuel(time, speed)

message = '{:.3f}'.format(fuel)

print(message)