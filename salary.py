#! /usr/bin/python
# calcula o salário de um funcionário a partir do id, horas trabalhadas e valor hora

employee = {'id': int(input()), 'hours': int(input()), 'hourValue': round(float(input()), 2)}

print('NUMBER = {}'.format(employee.get('id')))
print('SALARY = U$ {:.2f}'.format(employee.get('hours') * employee.get('hourValue')))