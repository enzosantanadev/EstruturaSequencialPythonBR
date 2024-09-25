media1 = float(input("qual a primeira nota? "))
media2 = float(input("qual a segunda nota?" ))
media3 = float(input("qual a terceira nota? "))
media4 = float(input("qual a quarta nota? "))

def media(media1, media2, media3, media4):
    return ((media1 * 3) + (media2 * 2) + (media3 * 3) + (media4 * 2)) / 10

resultado = media(media1, media2, media3, media4)

print(resultado)
