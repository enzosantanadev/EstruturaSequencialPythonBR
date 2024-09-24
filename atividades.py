salario = float(input("quanto vc ganha por hora? "))
trabalho = float(input("quantas horas vc trabalha no mes? "))

def calcular_salario(salario, trabalho):
    return salario * trabalho

salario_bruto = calcular_salario(salario, trabalho)
def imposto_renda(salario_bruto):
    return salario_bruto * 0.11

def inss(salario_bruto):
    return salario_bruto * 0.08

def sindicato(salario_bruto):
    return  salario_bruto * 0.05

imposto_renda_total = imposto_renda(salario_bruto)
inss_total = inss(salario_bruto)
sindicato_total = sindicato(salario_bruto)
salario_liquido_total = (salario_bruto - inss_total - sindicato_total - imposto_renda_total)



print(f"{salario_bruto} é seu salario bruto")
print(f"{imposto_renda_total} é oq vai pro imposto de renda")
print(f"{inss_total} é oq vai pro inss")
print(f"{sindicato_total} é oq vai pro sindicato")
print(f"{salario_liquido_total} é seu salario liquido")

