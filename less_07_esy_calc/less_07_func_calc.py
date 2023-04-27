# function for testing

# def citi_names(citi, region, population=None):
#     try:
#         if population:
#             if isinstance(population, int):
#                 location = citi + " " + region + " " + str(population) + " population"
#             else:
#                 location = citi + " " + region
#         else:
#             location = citi + " " + region
#
#     except:
#         location = citi + " " + region
#
#     return location.title()


def esy_calc_4(a, b, c=None):
    if c is None or c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "/":
        return a / b
    elif c == "*":
        return a * b

print(esy_calc_4(2, 3, "*"))

# print(citi_names("dfdf", "dfsd", 55))
# print(citi_names("dfdf", "dfsd", "df"))
# print(citi_names("dfdf", "dfsd"))
