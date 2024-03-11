#! /usr/bin/python
# calcula o valor a se pagar para duas peças

# obtem uma string com três valores que representam o id, a quantidade e o valor unitário do item
def getInput():
    rows = []
    
    for i in range(2):
        rows.append(input())

    return rows

# cria um item a partir de 3 valores passados como string
def createItem(values):
    id, quantity, value = values.split()

    id = int(id)
    quantity = int(quantity)
    value = round(float(value), 2)

    return {'id': id, 'quantity': quantity, 'value': value}

# calcula o valor total de um item
def totalCost(item):
    return item.get('quantity') * item.get('value')

# main
data = getInput()
items = []
total = 0

# cria uma lista de items a partir do input
for i in range(len(data)):
    items.append(createItem(data[i]))
    total += totalCost(items[i])

print('VALOR A PAGAR: R$ {:.2f}'.format(total))