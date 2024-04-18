
class Point:
  def __init__(self, num, num2, name): #CONSTRUCTOR
    self.num = num
    self.num2 = num2
    self.name = name
    
  def multiply(self):
    print(self.num * self.num2)
  
  def add(self):
    print(self.num + self.num2)
  
  def me(self):
    print(self.name)
    
point1 = Point(45, 98, 'John')

point1.add()
point1.multiply()
point1.me()

point2 = Point(4, 8, "Bob")

point2.add()
point2.multiply()
point2.me()