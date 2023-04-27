def esy_calc():
    a = float(input("input first number "))
    b = float(input("input second number "))
    calc_operator = str(input("input operator: +, -, /, * "))
    c = 0
    if calc_operator == "+":
        c = a + b
    elif calc_operator == "-":
        c = a - b
    elif calc_operator == "/":
        c = a / b
    elif calc_operator == "*":
        c = a * b
    else:
        c = "Error! Try ones more time, please!"

    print(c)
    text_calc = open("esy_calc.txt", "a")
    text_calc.write(str(a) + " ")
    text_calc.write(calc_operator + " ")
    text_calc.write(str(b) + " ")
    text_calc.write("= " + str(c) + "\n")
    text_calc.close()


while True:
    esy_calc()
