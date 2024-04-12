option = ''

while option.upper() != 'QUIT':
  option = input('> ')
  if option.upper() == 'HELP':
    print("""Start - To start car
Stop - To stop car
Quit - To quit """)
    
  elif option.upper() == 'START':
    print('Car has started!')
  elif option.upper() == 'STOP':
    print('Car has stopped!')
  else:
    print('I do not understand...')
else:
  print('You quit!')