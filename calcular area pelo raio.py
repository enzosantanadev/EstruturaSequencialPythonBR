pi = 3.14
raio = float(input("qual o raio"))
def calcular_area(pi, raio):
    return pi*raio**2
resultado = calcular_area(pi, raio)

print(f"a area do circulo de raio {raio} é {resultado}")
