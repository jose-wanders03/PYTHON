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
     

      

  