number1 = int(input("digite um numero inteiro"))
number2 = int(input("digite um numero inteiro"))
number3 = float(input("digite um numero real"))

def calculoA(number1, number2):
    return  (number1 * 2) * (number2 / 2)

def calculoB(number1, number3):
    return (number1 * 3) + (number3)

def calculoC(number3):
    return  (number3**3)


resultadoA = calculoA(number1, number2)
resultadoB = calculoB(number1, number3)
resultadoC = calculoC(number3)
print(f"o resultado A é {resultadoA}")
print(f"o resultado B é {resultadoB}")
print(f"o resultado C é {resultadoC}")
