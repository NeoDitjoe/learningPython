name = 'John Smith'
age = 45
status = 'new patient'

patient = "We check in a patient named %s. \nHe's %i years old and is a %s" %(name, age, status)

print(patient)
print(' ')

#Formatted string
print(f"We check in a patient named {name}. \nHe's {age} years old and is a {status}")

#get length
length = len(patient)
print(length)

#Long string
longStr = '''
This is a long string.

There is an empty line on top of this line.
This is so cool. 4Real
'''

print(longStr)

#Get Character
str = 'Cozy4Real'
print(str[0:4])
print(str[4:])
print(str[3])
print(str.replace('4', 'The'))
print('Cozy' in str) #includes

#input
# name = input('what is your name? ')

# age = input('Hi %s which year were you born? ' %(name))

# calculator = 2024 - int(age)

# print('Okay %s You are %s years old' %(name ,calculator))

###Numbers