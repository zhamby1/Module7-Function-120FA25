#order does matter when using multiple parameters depending on the program
#adding is not a big deal because of the associative property
#subtraction is different

def subtract_numbers(num1,num2):
    answer = num1 - num2
    print(answer)


#this can lead to two different answers if we are using the same values, because in subtraction...order matters
#remember, the first argument you give this function will represent num1, and the second will represent num2

subtract_numbers(10,5)

subtract_numbers(5,10)

# this program will calc a total value and display the user and their total for their purchase

def calc_total(name,total,tax):
    total_with_tax = total + (total * tax)
    print(name, "your total with tax is: ", total_with_tax)

my_name = input("Please tell me your name ")
purchase_total = float(input("Please tell me your total purchase amount "))
purchase_tax = float(input("Please tell me your tax rate using a decimal value "))


calc_total(my_name,purchase_total,purchase_tax)