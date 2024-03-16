#! /usr/bin/python

distance = int(input())
fuel = float(input())
ratio = distance / fuel

message = '{ratio:.3f} km/l'
print(message.format(ratio = ratio))