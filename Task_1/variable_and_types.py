# types of variables 
"string"
"floats"
"interger"
"boolean"
"lists"

# numbers

myint = 7          # interger
print (myint)

myfloat = 7.0      #float
print (myfloat)
myfloat = float(7)
print(myfloat)

#strings 

mystring = 'hello'   #for strings you an use apostrophe
print (mystring)  
mystring = "hello"   #you can also use speach marks 
print(mystring)



one = 1           #using numbers strings can allow you
two = 2           # to proform simple operations 
three = one + two 
print (three)

hello = "hello"
world = "world"
helloworld = hello + "" + world
print(helloworld)

#thought you can do simple operation like this you 
#can't do operation with both strings and numbers 
def mixing_operation () :
    one = 1
    two = 2
    hello = "hello"
    print (one + two + hello)

try: 
    mixing_operation ()
except:
    print ("[                                                       ]")
    print ("  Exception catching   ")

#exercie

def exercise_before ():
    mystring = None
    myfloat = None
    myint = None
    
    # testing code
    if mystring == "hello":
        print("String: %s" % mystring)
    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %f" % myfloat)
    if isinstance(myint, int) and myint == 20:
        print("Integer: %d" % myint)

print ("[                                                     ]")

def exercise_after ():
    mystring = "hello"
    myfloat = 10.0
    myint = 20
    
    # testing code
    if mystring == "hello":
        print("String: %s" % mystring)
    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %f" % myfloat)
    if isinstance(myint, int) and myint == 20:
        print("Integer: %d" % myint)

exercise_after ()