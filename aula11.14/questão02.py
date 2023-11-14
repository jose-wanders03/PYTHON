# Faça um codigo que cria uma lista de 10 numeros reais e imprima só os pares e depois só os impares.

# Criar uma lista de 10 números reais
numeros_reais = [1.5, 2.0, 3.3, 4.2, 5.6, 6.8, 7.1, 8.9, 9.4, 10.7]
numero = [ ]
# Imprimir números pares
pares = [numero for numero in numeros_reais if numero % 2 == 0]
print("Números pares:", pares)

# Imprimir números ímpares
impares = [numero for numero in numeros_reais if numero % 2 != 0]
print("Números ímpares:", impares)