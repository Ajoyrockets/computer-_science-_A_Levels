user_name = input("Enter your name:")
subject = input("The subject that you have need to go to:")

if subject == "computing" :
    print(f"{user_name},you should go to room 401")
elif subject == "music" :
    print(f"{user_name},you should go to room 404")
elif subject == "history" :
    print(f"{user_name},you should go to room 302")
elif subject == "english" :
    print(f"{user_name},you should go to room 345")
else:
    print("Sorry don't know what subject you are doing")