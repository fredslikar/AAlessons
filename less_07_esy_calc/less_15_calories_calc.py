def calory_calk(name, get_calory, loose_calory):
    if get_calory > loose_calory:
        return name + " get fat"
    elif get_calory < loose_calory:
        return name + " get theen"


persons = ["Ivan", 1444, 3333]
print(calory_calk("Andrey", 2000, 2050))
print(calory_calk(*persons))


def multiply_numbers(*arg):
    result = 1
    list1 = []
    for f in arg:
        list1.append(f)
        result = f * result
    return "result is " + str(result) + "\nlen of list of args is " + str(len(list1))


print(multiply_numbers(100, 20, 100, 10000, 250, 0.0003, -1))
