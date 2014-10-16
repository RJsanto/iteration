#Ricky Santos
#16/10/2014
#N factorial

number = int(input("please enter a number: "))
total = 0
number_2 = number

for count in range (number):
    total = number_2 * (number_2 + 1)
    number_2 = number_2 - 1
    if number >0:
        print (total)


