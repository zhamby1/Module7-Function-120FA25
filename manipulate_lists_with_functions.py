#we can also manipulates lists or data using functions
#for instance...lets build on the averaging program we have a make that a function

#so far we have had the user put in values individually through either a loop or as individual variables
#now lets us a list to calculate an average

def average(average_list):
    my_average = 0
    sum = 0
    for number in average_list:
        sum = sum + number

    my_average = sum / len(average_list)
    print("Your average is", my_average)


number_list = [10,40,586,74,68]
number_list2 = [10.54, 798.7, 56.4, 77.8,88.6,99.2]

average(number_list)
average(number_list2)