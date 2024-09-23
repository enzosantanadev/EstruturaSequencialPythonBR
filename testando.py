fahrenheit = float(input("informe a temperatura em fahrenheit"))

def transformar_temperatura(fahrenheit):
    return 5 * ((fahrenheit-32) / 9)
resultado = transformar_temperatura(fahrenheit)

print(resultado)



