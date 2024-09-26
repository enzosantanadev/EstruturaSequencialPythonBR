import math

area = float(input("digite o tamanho da área a ser pintada (em metros quadrados): "))

litros_por_metro = 6
capacidade_lata = 18
preco_lata = 80.00
preco_galao = 25.00
capacidade_galao = 3.6
litros_necessarios = area / litros_por_metro

latas_necessarias = math.ceil(litros_necessarios / capacidade_lata)
galoes_necessarios = math.ceil(litros_necessarios / capacidade_galao)
custo_em_galoes = galoes_necessarios * preco_galao
custo_em_latas = latas_necessarias * preco_lata

print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"preço total: R$ {custo_em_latas: .2f}")

print(f"Quantidade de galoes necessários: {galoes_necessarios}")
print(f"preço total: R$ {custo_em_galoes: .2f}")

if (custo_em_latas > custo_em_galoes):
    print("vc de comprar em galoes")
elif (custo_em_latas < custo_em_galoes):
    print("vc deveria comprar em latas")
else:
    print("tanto faz mano msm preço")
