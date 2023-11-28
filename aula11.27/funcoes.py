# funções são blocos de codigos que são executados somente quando são chamados 
# parametro: def
# obs: as funções devem ter prioridade no código

def media( nota01, nota02, nota03):
    media = (nota01 + nota02 + nota03) / 3
    return media

nota01 = int(input('Informe a primeira nota: '))
nota02 = int(input('Informe a segunda nota: '))
nota03 = int(input('Informe a terceira nota: '))

print (media(nota01, nota02, nota03))


def calcula_horas_extras(quantidades_horas, valor_da_hora):
    horas = float(quantidades_horas)
    taxa = float(valor_hora)

    if horas >= 40:
        valor_receber = ( horas - 40) * taxa
        return valor_receber
    
    
quantidades_horas = float(input('Informe o total de horas trabalhadas:'))
valor_da_hora = float(input('Informe o valor da taxa do colaborador: '))

salario = 1400.00
print(salario + calcula_horas_extras(quantidades_horas, valor_da_hora))

    
    