import math

arquivo = float(input("qual o tamnho do arquivo em MB: "))
internet = float(input("qual a sua internet em Mbps: "))
arquivo_Mb = arquivo * 8

def calculo(arquivo_Mb, internet):
    return arquivo_Mb / internet
resultado = (calculo(arquivo, internet)) / 60

print(f"a velocidade de download é {resultado} minutos")


