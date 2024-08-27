#basic operation

#arthemitic opertation

number = 1 + 2 * 3 / 4.0 # python does do bidmaths
print (number)

remainder = 11 % 3  # using % will give the remainder
print (remainder)   # of the division of 2 numbers

squared = 7 ** 2 # using two * tells python to do it 
cubed = 2 ** 3   # as a power and not mutiplcation can 
print(squared)   #also be done using ^
print(cubed)

lotsofhellos = "hello" * 10 # mulitpling a string will tell
print(lotsofhellos)  # python to print the string mulitple times 

even_numbers = [2,4,6,8]  # adding two lists in python will
odd_numbers = [1,3,5,7]   # just add all the variables in the
all_numbers = odd_numbers + even_numbers #list as 1 big set 
print(all_numbers)

print([1,2,3] * 3) #this makes it that python prints the list's 
                   # content 3 times 

#exercise

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")