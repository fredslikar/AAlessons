import json


nums = [2, 3, 23, 54, 54, 3, 6, 31]

filename = "file.json"
with open(filename, "w") as f:
    json.dump(nums, f)

filename = "file.json"

with open(filename, "r") as f:
    nums_new = json.load(f)

print(nums_new)



