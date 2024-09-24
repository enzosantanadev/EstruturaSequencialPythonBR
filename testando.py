number1 = int(input("digite um numero inteiro"))
number2 = int(input("digite um numero inteiro"))
number3 = float(input("digite um numero real"))

def calculoA(number1, number2):
    return  (number1 * 2) * (number2 / 2)

def calculoB(number1, number3):
    return (number1 * 3) + (number3)

def calculoC(number3):
    return  (number3**3)

resultado = calculoC(number3)
print(resultado)