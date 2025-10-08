#lets say you want to use a function in your program..there are a couple of ways to organize this
# 1 - to write most of your defined functions at the very top of your program, and call them after they are defined
#Problem is - it gets kind of messy and hard to maintain...as a beginner this is fine.

#2 - Separate your functions out into different files, and have a 'main' file that uses those functions
# This is often easier to troubleshoot,read, and collaborate

#When we do this, we will be making something called a module
#aka separated pieces that can be used across one or multiple files
#these basically can be the same thing as a function, it is just located in a different file
#if something is a module in python, it almost always needs to be a return function



def add(number1,number2):
    sum = number1 + number2
    return sum