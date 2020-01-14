input1 = input("Wage: ")
moneyEarned1 = float(input("Money you earned this month: "))
yearly1 = moneyEarned1*12

input2 = input("Expense 2: ")
monthly2 = float(input("Tithing: "))
yearly2 = monthly2*12*0.10

input3 = input("Expense 3: ")
fastOffering3 = float(input("Fast Offering: "))
yearly3 = fastOffering3*12

input4 = input("Expense 4: ")
monthly4 = float(input("Expense 4 Monthly Amount: "))
yearly4 = monthly4*12

input5 = input("Expense 5: ")
monthly5 = float(input("Expense 5 Monthly Amount: "))
yearly5 = monthly5*12

input6 = input("Expense 6: ")
monthly6 = float(input("Expense 6 Monthly Amount: "))
yearly6 = monthly6*12

input7 = input("Investments: ")
savings7 = moneyEarned1 - monthly2 - fastOffering3 - monthly4 - monthly5 - monthly6
yearly7 = savings7*12

print "\n"

print "Personal Budget"

print "======================================"
print " Income" + "       Month" + "      Year"
print "======================================"

print "%-10s $%-10.2f $%-10.2f" % (input1, moneyEarned1, yearly1)


print "======================================"
print " Expenses" + "       Month" + "      Year"
print "======================================"

print "%-10s $%-10.2f $%-10.2f" % (input2, monthly2, yearly2)
print "%-10s $%-10.2f $%-10.2f" % (input3, fastOffering3, yearly3)
print "%-10s $%-10.2f $%-10.2f" % (input4, monthly4, yearly4)
print "%-10s $%-10.2f $%-10.2f" % (input5, monthly5, yearly5)
print "%-10s $%-10.2f $%-10.2f" % (input6, monthly6, yearly6)

print "======================================"
print " Savings" + "       Month" + "      Year"
print "======================================"

print "%-10s $%-10.2f $%-10.2f" % (input7, savings7, yearly7)
