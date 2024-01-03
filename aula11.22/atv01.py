# Faça um programa que peça 10 numeros inteiros, calcule e mostre a quantidade de numeros pares e a quantidade de numero impares

contador_par = 0
contador_impar = 0
for i in range(1,11):
    numero = int(input(f'Informe o {i} numero'))
    if numero % 2 ==0:
        contador_par += 1 
    else:
        contador_impar +=1
    print(f'Quantidade de numero par é: {contador_par} ')
    print(f'Quantidade de numeros impares é: {contador_impar}')
     


numero_secreto = 42
chute = input("Digite seu número")
print("Você digitou ", chute)
if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")

minha_idade = 26
idade_namorado = 25
if(minha_idade == idade_namorado):
    print('temos idades iguais')
else:
    print('temos idades diferentes')


numero1 = 10
numero2 = 10
if(numero1 == numero2):
    print("São números iguais")


idade1 = 10
idade2 = int("20")
print(idade1 + idade2)


nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)
nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome)
nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome, sep="_")
    