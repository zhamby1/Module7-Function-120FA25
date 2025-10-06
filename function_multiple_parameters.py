#multiple parameters are separated by a ,
#lets create a function that can take two numbers in, and add them together
#multiple parameters are based on their position in the ()

def add_numbers(num1,num2):
    sum = num1 + num2
    print(sum)


#functions are great because we may not know where the data is coming from, but just that we want to add two numbers

#lets look at all the ways we can use this function

#raw values - we base what a parameter is tied to what argument based on its position
#in other words we know that we need to values, and the first value will be num1, and the second value will be num2
#thus we can just stick in raw values if we wish
add_numbers(7,6)

#I can use variables
number1 = 87
number2 = 10

add_numbers(number1,number2)

# we can also use inputs, as long as they are converted to a numerical type or calculable value
input_num_1 = int(input("Give me your first number "))
input_num_2 = int(input("Give me your second number "))
add_numbers(input_num_1,input_num_2)
