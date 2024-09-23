media1 = float(input("digite a primeira nota"))
media2 = float(input("digite a segunda nota"))
media3 = float(input("digite a terceira nota"))
media4 = float(input("digite a quarta nota"))

def calcular_media(media1,media2,media3,media4):
    return((media1 + media2 + media3 + media4)/4)

resultado = calcular_media(media1,media2,media3,media4)
print(f"o resultado da media é {resultado}")
