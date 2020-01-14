print "Monthly Budget"

print "===================================="
print " Item" + "      Month" + "       Year"
print "===================================="

input1 = 'Taxes'
yearly1 = 120
monthly1 = yearly1 /12

input2 = 'Tithing'
yearly2 = 200
monthly2 = yearly2 /12

input3 = 'Mortage'
yearly3 = 500
monthly3 = yearly3 /12

print "%-10s $%-10.2f $%-10.2f" % (input1, monthly1, yearly1)
print "%-10s $%-10.2f $%-10.2f" % (input2, monthly2, yearly2)
print "%-10s $%-10.2f $%-10.2f" % (input3, monthly3, yearly3)