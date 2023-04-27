import json
import random

user_name_list = []
z = random.randint(0, 10)
user_name_file = "user_name_file_" + str(z) + ".json"


def get_user_name():
    user_name = input("Please, input your name: ")

    with open(user_name_file, "w") as f:
        json.dump(user_name, f)
        print("We remember you as " + user_name)


def check_user_file():
    try:
        with open(user_name_file) as f:
            user_name_list = json.load(f)
            print("Your name is " + user_name_list)
            check_name = input("Is it your name? Input 'y' or 'n' ")
            if check_name == "y" or check_name == "Y":
                print("We are greeting you " + user_name_list)
            else:
                get_new_user_name()
    except:
        get_user_name()


def get_new_user_name():
    x = random.randint(0, 10)
    user_name_file = "user_name_file_" + str(x) + ".json"
    user_name = input("Please, input your name: ")
    with open(user_name_file, "w") as f:
        json.dump(user_name, f)
        print("We remember you as " + user_name)


check_user_file()
