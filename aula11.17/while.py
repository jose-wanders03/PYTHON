contador = 0
while contador <= 10:
# enquanto o contador for menor ou igual a 10 faça:
    nota = float(input('Informe uma nota: '))
    if nota < 0 or nota > 10:
        print('Sua nota não foi suficiente para continuar')
        break 
    contador = contador + 1


aluno = 1
while aluno <= 20:
    idade = int(input(f'Qual idade do aluno {aluno}?'))
    if idade > 13:
        print(f' A idade do aluno {aluno} e {idade}. E maior que 13.')
    aluno = aluno + 1
print('Fim da questão 01')