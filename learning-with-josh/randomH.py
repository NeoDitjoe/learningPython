#random
import random

keeper = 0
keeper2 = 0
choice = ['John', 'Mary', 'Bob', "Cozy"]

for i in range(4):
  keeper+= random.random()
  keeper2+= random.randint(100, 1000)
  
  
print(keeper)
print(keeper2)
print(random.choice(choice))

# challenge

class Dice:
  def roll(self):
    random_Int = random.randint(1, 6)
    random_IntB = random.randint(1, 6)
    
    return (random_Int, random_IntB)


dice = Dice()

print(dice.roll())