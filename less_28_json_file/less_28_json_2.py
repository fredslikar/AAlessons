import json

username = input("Input your name: ")

users = "file2.json"
with open(users, "w") as f:
    json.dump("We remember your name as \n", f)
    json.dump(username, f)
print(users)

