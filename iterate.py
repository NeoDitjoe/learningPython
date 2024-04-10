# while
num = 1

while num <= 10:
  print(num)
  num += 1




# #for
for i in range(num, 21):
  print('what is this %i' %(i))





#Iterate over a string of objects
people = [{"name": "neo", "age": 23}, {"name": "cozy", "age": 23}]

for person in people:
  print('My name is %s I am %i Years old' %(person['name'], person['age']))




numB = 1

while numB <= 5:
  print('*' * numB)
  numB += 1
  