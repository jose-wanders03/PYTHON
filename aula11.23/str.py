# count - função é contar quantas vezes um determinado caractere aparece em uma string
# upper e a lower - dois metodos que deixam a string toda em maiuscula ou a string toda minuscula
# find - buscar por uma expressão dentro da frase
# replace - é utilizado para realizar alterações dentro da string
# capitalize - deixa a primeira letra da frase minuscula
# 


frase = " A banana é amarela e o abacate é verde."
letra = 'a'
print(f' A letra "{letra}" aparece {frase.count(letra)} vezes na frase" {frase.count(letra)}".')
achei = frase.find('ana')
print(frase.find ('ana'))

if achei >= 0:
    print(f'A expressão foi encontrada no indice {achei}')
else:
    print(f'A expressão NÃO foi encontrada na frase')

nova_frase = frase.replace(' banana ', '  maracuja ')
nova_frase2 = frase.replace(' abacate ', ' manga ')
nova_frase2 = frase.replace(' ', ' ')
print(frase)
print(nova_frase)
print(nova_frase2)
print(frase.capitalize())
print(frase.split())


