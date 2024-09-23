salario = float(input("quanto vc ganha por hora"))
trabalho = float(input("quanto vc trabalha por mes"))

def calcular_salario(salario, trabalho):
    return salario * trabalho

salario_total = calcular_salario(salario, trabalho)

print(salario_total)
