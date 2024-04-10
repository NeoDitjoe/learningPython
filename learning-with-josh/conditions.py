
good_credit = False
high_income = True
price = 1000000

if good_credit and high_income:
  down_payment = price/100*5
elif good_credit or high_income:
  down_payment = price/100*10
else: 
  down_payment = price/100*20

cost = 'Down payment: R %i' %(down_payment)
print(cost)

name = 'Cozy4Real'

if len(name) < 3:
  message = 'Name must be 3 characters or more!'
elif len(name) > 12:
  message = 'Name must be 12 or less characters!'
else:
  message = 'Name looks good!'
  
print(message)

#input and conditions
weight = input('Enter your weight: ')
input = input('is this (L)pounds or (K)kilograms? ')

if input.upper() == 'L':
  output = 'You are %i Kg' %(int(weight) *  0.45359237)
elif input.upper() == 'K':
  output = 'You are %i Lbs' %(int(weight) / 2.2046)
  
print(output)