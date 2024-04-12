names = [
  "Toshiaki",
  "Juliana",
  "Yuji",
  "Bruno",
  "Kaio",
  "Neo"
]

names[0] = 'Neo' # change the item
names.append('Mary') # add items
names.insert(2, 'John')
names.remove('Bruno')

print(names.count('Neo'))
print(names.index('Neo')) 
print(names) 
print(names[3:]) # from 3 to end
print(names[2:4]) # from 3 to 4
print(names[:3]) #from the beginning



# Challenge: Find the largest number in a list

numbers = [ 4, 7, 20, 17, 8 ]
largest_number = 0

for x in numbers:
    if largest_number < x:
      largest_number = x
      
print(largest_number)



# Challenge: Remove Duplicates

no_duplicates = []

for item in names:
  if item not in  no_duplicates:
    no_duplicates.append(item)
print(no_duplicates)