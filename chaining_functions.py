#in python, we can use return type functions to pass data to other functions
#this is known as functions as first class citizens, or higher-order functions
#in reality, this basically means the ability to chain functions
#this is really popular with the function 'style' of programming

#this functions will add items together and then we can add tax
def add_items(item1,item2,item3):
    total = item1 + item2 + item3
    return total #we are going to return this data into another function

def add_tax(total):
    tax = total * 0.06
    total_with_tax = total + tax
    #terminating function - void function..you could return this into another variable..but we just want this to display
    print("Your total with tax is", total_with_tax)

#because add_items is a return function...we can return data into another function as long as that function has a parameter for that data
add_tax(add_items(5.00,10.50,8.64))