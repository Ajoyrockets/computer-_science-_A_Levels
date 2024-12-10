import string

MY_STACK =[]
PUSH_ITEM = ""
POP_ITEM = ""



def push_items ():
    try:
        iteration_push_count = int(input("How many items do you want to push onto the stack? "))
        if iteration_push_count > 0:
            print("Please enter a positive number.")
            return
        for _ in range(iteration_push_count):
            push_item = input("Input what you want to add to the stack: ")
            MY_STACK.append(push_item)
        print("Items added successfully. Current Stack:", MY_STACK)
    except ValueError:
        print("Invalid input. Please enter another number.")
        push_items ()

def pop_item():
    POP_ITEM = MY_STACK.pop(-1)
    print(POP_ITEM)
    print(MY_STACK)

def operation(MENU_ITEM,):
    if MENU_ITEM == "1":
        push_items()
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
    MENU_ITEM = input("Type in ether 1 , 2 or 3:")
    operation(MENU_ITEM)
   
   
if __name__ == "__main__":
    main()