#Ricky Santos
#16/10/2014
# program to prompt for 8 numbers and report the total to the user

#improved code
total = 0
number = 0

for count in range (8):
    number = int(input("Please enter a number: "))
    total = total + number

print ("the total is {0}".format(total))


