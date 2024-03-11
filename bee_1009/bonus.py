#! /usr/bin/python
# calcula o salário com bônus a partir do salário e vendas

def compensation(employee):
    fee = 0.15
    return employee.get('salary') + employee.get('sales') * fee

employee = {'name': input(), 'salary': round(float(input()), 2), 'sales': round(float(input()), 2)}

print('TOTAL = R$ {:.2f}'.format(compensation(employee)))