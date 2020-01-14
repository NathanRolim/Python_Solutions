import math
pi = math.pi

def displayWelcome():
  print "Welcome to the calculator \n"
  
def calcAreaCircle(area):
  area = pi * radius * radius
  return area
  
def calcPerimeterCircle(perimeter):
  perimeter = 2 * pi * radius
  return perimeter

def calcAreaSquare(area):
  area = side ** 2
  return area
  
def calcPerimeterSquare(perimeter):
  perimeter = 4 * side
  return perimeter
  
def calcAreaRect(self, area):
  area = width * height
  return area
  
def calcPerimeterRect(self, perimeter):
  perimeter = 2 * (width + height)
  return perimeter
  
def calcAreaTriangle(self, area):
  area = (base * height) / 2
  return area

# =====================================================================

# Main Code - DO NOT EDIT ANYTHING BELOW.  Add your functions above

displayWelcome()

radius = 3.56

area = calcAreaCircle(radius)

perimeter = calcPerimeterCircle(radius)

print 'Circle : area = %.2f, perimeter = %.2f' % (area, perimeter)


side = 9.23

area = calcAreaSquare(side)

perimeter = calcPerimeterSquare(side)

print('Square: area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


width = 2.9

height = 14.22

area = calcAreaRect(width, height)

perimeter = calcPerimeterRect(width, height)

print('Rectangle: area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


base = 7.97

height = 5.31

area = calcAreaTriangle(base, height)

print('Triangle : area = {0:.2f}'.format(area))