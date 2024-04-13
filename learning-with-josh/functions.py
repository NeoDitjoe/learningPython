def emojier(msg):
  message = msg
  words = message.split(' ')

  emojis = {
    ':)': '😁',
    ':(': '🥲'
  }

  output = ''

  for word in words:
    output += emojis.get(word, word) + ' '

  return output
  
  
print(emojier(input('> ')))
print(emojier("Neo Ditjoe :)"))