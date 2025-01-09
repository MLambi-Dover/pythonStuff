import math

#this declares the class
class Circle:
  def __init__(self, radius = 1.0):#constructor sets variable values when created, will be 1 if no number is passed in
    self.radius = radius  #variable is public - directly accesible outside of the class

  def getPerimeter(self):#will return the perimeter
    return 2.0 * self.radius * math.pi

  def getArea(self):#will return the area
    return self.radius * self.radius * math.pi
  
  def setRadius(self, radius): #allows for setting of radius, cannot be done directly
    if radius > 0: #make sure radius isn't negative or 0
      self.radius = radius
  
  def getRadius(self):#allows for access to the radius variable although it can be accessed directly as a public variable
    return self.radius

  def __str__(self):#format for how the object will be printed
    return "Radius: "+ str(self.radius) + " | Perimeter: " + str(round(self.getPerimeter(), 3)) + " | Area: " + str(round(self.getArea(), 3))
