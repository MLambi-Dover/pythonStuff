import math


#this declares the class
class CirclePrivate:
  def __init__(self, radius = 1): #constructor sets variable values when created, will be 1 if no number is passed in
    self.__radius = radius

  def getPerimeter(self): #will return the perimeter
    return 2 * self.__radius * math.pi

  def getArea(self): #will return the area
    return self.__radius * self.__radius * math.pi

  def setRadius(self, radius): #allows for setting of radius, cannot be done directly
    if radius > 0: #make sure radius isn't negative or 0
      self.__radius = radius

  def getRadius(self): #allows for getting radius because cannot be done directly
    return self.__radius

  def __str__(self):#format for how the object will be printed
    return "Radius: "+ str(self.__radius) + " | Perimeter: " + str(round(self.getPerimeter(),3)) + " | Area: " + str(round(self.getArea(),3))
