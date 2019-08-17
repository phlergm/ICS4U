number_sum = 0

def sum_digits(x): 
    global number_sum
    if int(x/10) == 0: 
        number_sum += x
        return number_sum
    if x <= 0:
        return -1
    else: 
        number_sum += (x % 10)
        x = int(x/10)
        return sum_digits(x)
    
number = int(input("whta nuber \n"))
print(sum_digits(number))
