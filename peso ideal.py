
altura = float(input("qual a sua altura (em metros): " ))
genero = input("vc é homem? ")

def peso_ideal(altura, genero):
    if genero == "sim":
        return (72.7*altura) - 58
    else:
        return (62.1*altura) - 44.7

resultado = peso_ideal(altura, genero)

print(resultado)
