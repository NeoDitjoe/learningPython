
try:
  num = int(input('Enter > '))
  print(f'I am {num}% good!')
  print(100/num)
except ZeroDivisionError:
  print('cannot devide by zero')
except ValueError:
  print('Invalid! Enter Integer!')
except:
  print('Error')