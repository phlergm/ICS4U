#-----------------------------------------------------------------------------
# Name: Humza Anwar
# Purpose: To find the sum of the digits of a given number
#
# References: 
#
# Author: Humza Anwar
# Created: 20/09/18
# Updated: 25/09/18
#-----------------------------------------------------------------------------
number = input("What p o s i t i v e number u wanna do \n")
number_length = len(number)
sum_of_digits = 0
number = int(number)

print ("--length = " + str(number_length))

while number_length > 0:
    print(number)
    if number < 0:
        sum_of_digits = -1
    if len(str(number)) == 1:
        sum_of_digits += number
    else: 
        sum_of_digits += (number % 10)
    number_length -= 1
    number = int(number/10)
		
print("sum of digits is " + str(sum_of_digits))


