############################################################
#     Name : Student Name                   Date: 3/23/21  #
#     Unit 8 Problems                                      #
#     Sample Circle Class                                  #
############################################################


#import class code from another repl.it file
from Circle import Circle
from CirclePrivate import CirclePrivate

print("\n\n")
#create a circle object called mycirc with public radius variable
mycirc = Circle(10.0)

#put problem code in a function so it can be easily commented out
#pass circle object into function so function can access it
def Problem1(acircle):
  #output circle radius directly, area and perimeter with methods
  print("Public variable Circle with radius " + str(acircle.radius) + ":")
  print("Area: " + str(round(acircle.getArea(),3)))
  print("Perimeter: " + str(round(acircle.getPerimeter(),3)))
  print(acircle)
  print()

  #change radius directly because public and output change
  acircle.radius = 20.0
  print("Change public variable Cirlce radius to " + str(acircle.radius) + ":")
  print("Area: " + str(round(acircle.getArea(),3)))
  print("Perimeter: " + str(round(acircle.getPerimeter(),3)))
  print(acircle)
  print()

#this calls problem function if commented out code will not run
Problem1(mycirc)

print("\n\n")


#put problem code in a function so it can be easily commented out
#Since the object was created in the file it is available globally so I do not have to pass it in
#this is not different from last method just a different approach
def Problem2():
  #create a circle object called mycirc2 with private radius variable
  mycirc2 = CirclePrivate(8.0)
  #output radius, area, perimeter with methods, cannot access radius directly
  print("Private variable Circle with radius " + str(mycirc2.getRadius()) + ":")
  print("Area: " + str(round(mycirc2.getArea(),3)))
  print("Perimeter: " + str(round(mycirc2.getPerimeter(),3)))
  print(mycirc2)
  print()

  #print(mycirc2.radius) #uncomment this line and get an error for trying to access private variable

  #try to change radius directly, doesn't work but creates a variable called mycirc2.radius
  #output results to show failed change attempt
  mycirc2.radius = 16.0
  print("Tried to change Private variable Cirlce radius to 16: Radius = " + str(mycirc2.getRadius()) + ":")
  print("Area: " + str(round(mycirc2.getArea(),3)))
  print("Perimeter: " + str(round(mycirc2.getPerimeter(),3)))
  print()
  print(mycirc2)

  #use set method to successfully change radius
  mycirc2.setRadius(16.0)
  print("Changed Private variable Cirlce radius to 16: Radius = " + str(mycirc2.getRadius()) + ":")
  print("Area: " + str(round(mycirc2.getArea(),3)))
  print("Perimeter: " + str(round(mycirc2.getPerimeter(),3)))
  print()
  print(mycirc2)

#this calls problem function if commented out code will not run
Problem2()
