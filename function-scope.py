#Functions can also be a series of statements that can allow us to call it to calculate something
#add two numbers together

#scope - where data is located in a program, and who has access to it
#this is a global variable...it can be used with many functions and retain its value

z = 42 #global variable

def add_calculation():
    x = 5
    y = 6
    sum = x + y + z
    print(sum)

def subt_calculation():
    x = 10 #having the same variable name in different functions is ok.
    y = 4
    answer = z - x - y
    print(answer)

add_calculation()

subt_calculation()