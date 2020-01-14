input1 = input("Item 1: ")
monthly1 = float(input("Item 1 Monthly Amount: "))
yearly1 = monthly1*12

input2 = input("Item 2: ")
monthly2 = float(input("Item2 2 Monthly Amount: "))
yearly2 = monthly2*12

input3 = input("Item 3: ")
monthly3 = float(input("Item 3 Monthly Amount: "))
yearly3 = monthly3*12

input4 = input("Item 4: ")
monthly4 = float(input("Item 4 Monthly Amount: "))
yearly4 = monthly4*12

input5 = input("Item 5: ")
monthly5 = float(input("Item 5 Monthly Amount: "))
yearly5 = monthly5*12

print "\n"

print "Monthly Budget"

print "======================================"
print " Item" + "       Month" + "      Year"
print "======================================"

print "%-10s $%-10.2f $%-10.2f" % (input1, monthly1, yearly1)
print "%-10s $%-10.2f $%-10.2f" % (input2, monthly2, yearly2)
print "%-10s $%-10.2f $%-10.2f" % (input3, monthly3, yearly3)
print "%-10s $%-10.2f $%-10.2f" % (input4, monthly4, yearly4)
print "%-10s $%-10.2f $%-10.2f" % (input5, monthly5, yearly5)