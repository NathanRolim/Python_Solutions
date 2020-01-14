name = raw_input("C for Circle, T for Triangle, or R for Rectangle: \n")

def areacalculator():
 
 if name == "C" or name == "c":
    radius = float(raw_input("Radius: "))
    circle_area = 3.14159265359 * radius * radius
    print "Circle area is: " + str(circle_area)
  
 elif name == "T" or name == "t":
    height = float(raw_input("Height: "))
    base = float(raw_input("Base: "))
    triangle_area = (base * height ) / 2
    print "Triangle area is: " + str(triangle_area)
  
 elif name == "R" or name == "r":
    height = float(raw_input("Height: "))
    base = float(raw_input("Base: "))
    rectangle_area = base * height
    print "Triangle area is: " + str(rectangle_area)
  
 else:
  print "Enter a available shape."
 
areacalculator()