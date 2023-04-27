glory = open("../less_07_esy_calc/esy_calc.txt", "a")
new_text = input("Input som text: ")
glory.write("\n" + new_text)
glory.write("\nHi? How are you?")

glory2 = open("../less_07_esy_calc/esy_calc.txt", "r")
print(glory2.read())

