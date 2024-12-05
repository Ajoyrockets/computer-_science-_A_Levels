#conditions 

x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True
# python uses bollean logic to evaluation conditions 
# The boolean vaules can be true or false 
# the == is the comparision 



name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

#the "and" and "or" boolean operators allows for 
#building more complex booleans

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#"in" operators could be used to cheakc if a 
#specifiec object exits usely in a list


statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

#python uses indentations insead of brackets with 
#the indentation being 4 spaces thought tab is allow
#use in some text editor 

#for exmaple:
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")



x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#The "is" does not mach the vaule of the variavle 
#unlike the == but they match the instants themselves

print(not False) # Prints out True
print((not False) == (False)) # Prints out False
# The "not" operator before a boolean expeersion is 
# inverted

# exercise 

# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")