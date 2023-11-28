# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caracteres "P", se seu argumento for positivo, e "N", se seu argumento for negativo.

def verificar_sinal(numero):
    numero = float(input('Digite um numero: '))
    if numero > 0:
        return 'P'
    elif numero <= 0:
        return 'N'
resultado = verificar_sinal(-5)
print(resultado)
