digits = input('Phone: ')

converter = [
  { 
    'digit': '0',
    'str':'zero'
  },
  { 
    'digit': '1',
    'str':'One'
  },
  { 
    'digit': '2',
    'str':'Two'
  },
  { 
    'digit': '3',
    'str':'Three'
  },
  { 
    'digit': '4',
    'str':'Four'
  },
  { 
    'digit': '5',
    'str':'Five'
  },
  { 
    'digit': '6',
    'str':'Six'
  },
  { 
    'digit': '7',
    'str':'Seven'
  },
  { 
    'digit': '8',
    'str':'Eight'
  },
  { 
    'digit': '9',
    'str':'Nine'
  },
]

results = []

for num in digits:
  for str_num in converter:
    if num == str_num.get('digit'):
      results.append(str_num.get('str'))

print(results)




# V2
covert = {
  '1': 'One',
  '2': "Two",
  '3': 'Three'
}

output = ''

for num in digits:
  output += covert.get(num, '!?') + ' '
print(output)