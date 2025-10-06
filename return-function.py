#create a function that adds three items together and returns it to an outside variable


#use a return function
#a return function must have something it returns it's value into
#a variable is a common choice
def add_items(item1,item2,item3):
    total = item1 + item2 + item3
    #in the past examples, we just print total...but maybe we need total for some other function or variable
    return total


#we can use another function to take in the answer from the previous function..this function can be a void function with our print statement
#we could also do the print statement outside of this function if it were a return function.
def total_with_tax(total,tax):
    total_with_tax = total + (total * tax)
    print(total_with_tax)

my_total = add_items(7,8,9)
total_with_tax(my_total,0.06)