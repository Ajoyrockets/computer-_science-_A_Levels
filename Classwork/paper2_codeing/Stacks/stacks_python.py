MY_STACK =[]
PUSH_ITEM = ""
POP_ITEM = ""

def push_item():
    try :
        number = int(input("input how many items you want to put on the stack:"))
    except:
        print("you inputted an invalid character try again")
        
    while number > 0 :
        number = number - 1
        PUSH_ITEM = input("Input what you want to be in the stack:")
        MY_STACK.append(PUSH_ITEM)
    else :
        print(MY_STACK)

        
def pop_item():
    if len(MY_STACK) == 0 :
        print("Please push some numbers into the stack")
    else:
        POP_ITEM = MY_STACK.pop(-1)
        print(POP_ITEM)
        print(MY_STACK)

def operation(MENU_ITEM):
    if MENU_ITEM == "1":
        push_item()
    elif MENU_ITEM == "2":
        pop_item()
    elif MENU_ITEM == "3":
        print(MY_STACK)
    elif MENU_ITEM == "4" :
        quit()
    else:
        print("invalid Number try again")
    main()

def main():
    print("""MENU:
Push Item -- 1
Pop Item  -- 2
See List  -- 3
Quit      -- 4""")
    MENU_ITEM = input("Type in ether 1 , 2, 3 or 4:")
    operation(MENU_ITEM)
   
   
if __name__ == "__main__":
    main()



"""
# assign list

with open('gfg.txt', 'w+') as f:
    
    # write elements of list
    for items in l:
        f.write('%s\n' %items)
    
    print("File written successfully")


# close the file
f.close()
"""