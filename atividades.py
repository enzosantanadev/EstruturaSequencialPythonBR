peso = float(input("qual o peso dos peixes? "))

def excesso_limite(peso):
    if peso > 50:
        return peso - 50
    else:
        return print("não há excesso")

excesso = excesso_limite(peso)
multa = excesso * 4
print(peso)
print(excesso)
print(multa)
