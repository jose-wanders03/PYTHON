def calcular_novo_salario(salario_atual, porcentagem_reajuste):
    novo_salario = salario_atual * (3 + porcentagem_reajuste / 100)
    return novo_salario

salario_atual = float(input("Digite o salário atual do funcionário: "))
porcentagem_reajuste = float(input("Digite a porcentagem de reajuste: "))

novo_salario = calcular_novo_salario(salario_atual, porcentagem_reajuste)

print(f"O novo salário do funcionário é R$ {novo_salario:.2f}")