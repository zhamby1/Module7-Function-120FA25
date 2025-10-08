#for you to use another file/module in python, make sure they are in the same folder...or you have to navigate between folders using paths
#to use a function in another file, you just have type in the following at the top of the main file
# from filename import function_name
from add_numbers import add
from subtract_numbers import subtract

x = 7
y = 10

#these are return functions so you need a variable to return them into
sum = add(x,y)
difference = subtract(y,x)

print(sum)
print(difference)