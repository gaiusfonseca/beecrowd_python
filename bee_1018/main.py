#! /usr/bin/python
# calcula a quantidade mínima de cédulas para se chegar a um valor


# calcula o máixmo de cédulas possível
def calculateBankNotes(bankNoteValue):
    global value
    quantity = 0

    while value >= bankNoteValue:
        value -= bankNoteValue
        quantity += 1

    return quantity

# cédulas possíveis 100, 50, 20, 10, 5, 2 e 1
bankNotes = [100, 50, 20, 10, 5, 2, 1]
quantities = [0, 0, 0, 0, 0, 0, 0]
messages = []

# imprime o valor original
value = int(input())
print(value)

# calcula a quantidade de cédulas para cada nota
for i in range(len(bankNotes)):
    quantities[i] = calculateBankNotes(bankNotes[i])
    message = '{:n} nota(s) de R$ {:.2f}'.format(quantities[i], bankNotes[i])
    message = message.replace('.', ',')
    messages.append(message)

# imprime a mensagem para cada cédula
for message in messages:
    print(message)