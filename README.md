# Functions

Functions are the way 'actions' are performed in a programming language.  They are often referred to as the 'verb' of the programming world. 

You have already used a few functions in this class.  For instance the print() function in Python, allows us to display something on screen

```python
print("Hello World") #displays Hello World on screen
```
You can differentiate a function from a variable by the () used in the function name.  if there is a word then a (), then it is usually a function.

```python 
x = 6 #variable
print(x) #function
```

The words or variables you use in-between the () are called arguments. Arguments are data that is passed to a function for processing.

Arguments can be used for more than just calculations.  For instance, the input() function uses arguments as a way to display a prompt to a user

```python
name = input("What is your name? ") #the text inside the () will display to the user in the form of a prompt
```
With that being said, a function can have many 'definitions' that can define how a function works in the programming world.  These are not scientific, but more describe what a function can do.

## Mathy Definition
A function takes data in, performs a calculation or process, and produces an output/answer

## Programming Definition / Characteristics

A function in the programming world can have the following characteristics or perform the following actions:

- Just like in math, a function can take data in, process it, and create an output.
- A function can also be a series of steps or statements that run when a function is called, with no necessary output or return value.
- A function can take data in, calculate a result, and pass/return that result to another variable or function.

## Overall SDEV Definition
A function in reusable code that can take data in, process it in some way, and either return that data into another function/variable or run a series of statements.

In addition to this, a function should be limited to perform on type of action or overall thing.

## Function Characteristic 1 - Reusable Series of Statements
Functions can be used to just have a block of code that can be called when the function name is called.  They do not have to process data, they can just be a series of statements.

This leads us to wondering how to create a function.  To create a function we first have to define it. In Python, we use the keyword 'def' followed by the function's name, and then ():. The function body MUST BE indented to be part of that function

```python
def sing_happy_birthday():
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday Dear Person")
    print("Happy Birthday to You")
```

This just defines the function, we have not yet run it.  To run/call a function, just type in it's name followed by the parenthesis.  We call these type of functions that just run statements void functions.

```python
sing_happy_birthday()
```

## Function Scope
Variable scope is important when understanding how functions work.  Scope basically means where data is located in the program, and who has access to it.

Anytime you define a variable within a defined function, that variable cannot be accessed/modified outside of the function it belongs to

```python
def add_calculation():
    x = 5
    y = 8
    sum = x + y
    print(sum)

add_calculation() #this works because we are calling the function

print(x) #this would lead to an error because we are trying to access something inside of another function

```

Why does this matter, or why is the a good thing?

1. It allows us to control what data is being processed and who has access to the data.
2.  It allows us to use the same variable name if they are in different functions
3. Allows us to create global variables that can be accessed by many functions if they are declared outside of any function

```python
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
```

## Function Characteristic 2 - Take Data in and Process It
So far, we have only grabbed data outside of a function when it is a global variable.  There is a much better alternative to this called using a parameter.

Often, when we need to pass data to a function (aka a function needs some data to process), we can use parameters as a way to pass some variable or data information to a function.

Parameters are just arguments that we have not used yet, and are defined on how we use them in the function body.

Arguments are just data that goes in between the () when we CALL OR USE a function.

Parameters are used when DEFINING a function, often though these terms are user interchangably

Parameters are placed inside of the () when DEFINING a function

We are using parameters to pass data.

Pass Data - Give the function some outside data to process

In Python, we can passs almost any type of data we want to it, including data structures like lists/arrays

As a way to remember how a parameter worsk, thing of it like a placeholder.  A parameter will tell you how much data you need, and how the data will be processed, but not WHAT THE DATA IS.

The syntax for adding parameters to a function is def function_name(parameter):

### Parameter Example
Lets look at a simple exmaple where a function takes in some text then shows it on screen using the happy birthday example

Instead of saying Happy Birthday Dear Person, we want Dear Person to be replaced with an actual person's name.

A parameter can be named whatever you want it to be...it is similar to a variable name.  It just doesn't have value untill you can the function.

We will us that word 'name' as a parameter for this function.  How this works is that whatever we want to do with the parameter that is surrounded by the (), we will put that in the function body.

```python
def sing_happy_birthday(name):
    print("Happy Birthday to You")
    print("Happy Birthday to You")
    print("Happy Birthday Dear", name)
    print("Happy Birthday to You")

#we can now use a variable to be used as an argument to the sing_happy birthday function

#This is really important, the variable names do not have to match the parameter name

#The purpose of creating a named parameter is just saying we are taking data in and doing this to the data

my_name = input("Please give me your name ")
sing_happy_birthday(my_name)

```

### Multiple Parameters
A function can have multiple parameters by places a comma (,) between each parameter

```python
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
```

Because positioning matters in a function call when using multiple parameters, make sure the order is correct depending on your program.

```python
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
```


## Function Characterstic 3 - Take Data In, Process It, and Return It Outside Of The Function

Functions can also return values into variables or other functions

Return value - the value that is returned to something outside of the function (often a variable)

To return a value we use the keyword....return

This is not too much different than a void function.  The only real difference is we are giving outside variables and functions some data result that we have caluclated or manipulated

```python

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
```
