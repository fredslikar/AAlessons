def esy_calc(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "/":
        if a > b:
            return a / b
        else:
            return "Ця программа не може ділити менше на більше число!!!"
    elif c == "*":
        return a * b


q = esy_calc(500, 300, "/")
print(q)
