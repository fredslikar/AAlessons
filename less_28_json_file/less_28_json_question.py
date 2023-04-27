import json

with open(user_name_file) as f:
    user_name_list = json.load(f)
    print("Your name is " + user_name_list)
    check_name = input("Is it your name? Input 'y' or 'n' ")
    if check_name == y:
        print("We are greeting you " + user_name_list)
    else:
        get_new_user_name()