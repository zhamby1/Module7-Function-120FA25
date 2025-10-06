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