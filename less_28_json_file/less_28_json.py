import json


def is_number(x):
    try:
        float(x)
        return True
    except:
        return False

for i in range(3):
    file_usnum = "usnum.json"
    try:
        with open(file_usnum) as f:
            num = json.load(f)
        if is_number(num):
            print("Your favorite number is " + str(num))
    except:
        for i in range(3):
            users_number = input("Input your favorite number: ")
            file_usnum = "usnum.json"
            if is_number(users_number):
                with open(file_usnum, "w") as f:
                    json.dump(users_number, f)
                    print("We remembered your number as " + str(users_number))
                    break
            else:
                print("Sorry, but You must number input, pleas...")
