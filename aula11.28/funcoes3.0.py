# Faça uma função que informe a quantidade de digitos de um determinado numero inteiro.

numero = input('Informe os numeros: ')
digito = len (numero)
print(f' A quantidade de digito foi: {digito}')

# Escreva uma função chamada gorjeta, que recebe o valor da conta de um restaurante, calcule e exibe a gorjeta do garçom, considerando 12% do valor da conta.

def calcular_gorjeta(valor_conta):
    gorjeta = valor_conta * 0.12
    print(f"A gorjeta do garçom é: R${gorjeta:.2f}")

valor_da_conta = float(input("Digite o valor da conta: R$ "))
calcular_gorjeta(valor_da_conta)