# For trabalha com intervalos!!!
# tem que possuir uma variavel de controle
# iter()
# next ()

nome = 'Wanderson'
letra = iter(nome)
print(next(letra))
print(next(letra))
print(next(letra))
print(next(letra))

for letra in nome:
    print(letra)

# enumerate () é um interador de indices e valores

lista_nomes = ['João', 'Pedro', 'Mateus', 'Judas', 'Tiago']

lista_enumerada = enumerate(lista_nomes)
print(lista_nomes)
print(list(lista_enumerada))

for item in lista_enumerada:
    print(item)

for item_lista in lista_enumerada:
    print(item_lista)




