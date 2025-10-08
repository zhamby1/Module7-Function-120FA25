#Can I use functions with lists..of course
#they work basically the same way as a normal function..they can be taken in as a parameter
#the only big difference is that you have to make sure to utilize techniques that you would normally do with a list
#The good thing about this is that you can shorthand some functions for lists, or create ways to iterate through lists that can be less complicated aka abstract

#For instance, maybe I am tired of utilizing a loop to print a list and i have multiple lists in my program.
#What I could do instead is create a function that just displays items in a list and call that function

#print any list
def print_list(single_list):
    for item in single_list:
        print(item)


def sum_list(a_list):
    sum = 0
    for item in a_list:
        sum = sum + item
    print(sum)


#now we can use this function for ANY type of list regardless of data type

groceries = ["milk","orange","bacon"]
scores = [100,40,77]
prices = [10.5,5.5,8.5]



print_list(groceries)
print_list(scores)

sum_list(scores)
sum_list(prices)

