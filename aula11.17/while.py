

contador = 0
while contador <= 10:
# enquanto o contador for menor ou igual a 10 faça:
    nota = float(input('Informe uma nota: '))
    if nota < 0 or nota > 10:
        print('Sua nota não foi suficiente para continuar')
        break 
    contador = contador + 1 



'''while True:
    nota = int(input('Informe a nota: ')) '''