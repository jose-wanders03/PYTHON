# Uma lista é representada pelos []
# O len - metodo que retorna a quantidade de itens de uma lista; obs: todo metodo por obrigação ele retorna algum valor
# obs: o append sempre coloca o valor atribuido para o final da lista
# append - metodo que insere itens no final da lista
# dell - remove pelo indice especifico da lista
# remove - remove um objeto especificado da lista
# pop - remove o ultimo objeto da lista, obs
# insert -  adiciona um objeto no inicio da lista

lista = []
print(lista, type(lista))
print(len(lista))

lista = ['front']
print(lista, type(lista))
print(len(lista))

lista = ['back']
print(lista, type(lista))
print(len(lista))

lista.append('front')
print(lista, type(lista))
print(len(lista))

lista.append('data')
print(lista, type(lista))
print(len(lista))

#           0       1      2    3    4
# REVERSE  -5       -4     -3   -2   -1
lista =  ['back', 'tarde', 21, True, 8.8]
print(f'a quantidade de alunas na turma é: {lista[2]}')
lista[2] = 22
print(lista)

lista [1] = False
print(list) 
lista[1] = ['Neyva', 'Alice', 'Lara', 'Paula', 'Geisa']
print(lista[1][2])

print(lista)
del lista[-2]
print(lista)
print(lista)
del lista[-2]
print(lista)
print(lista)
del lista[-2]
print(lista)

lista.remove('back')
print(lista)
lista.append('back')
lista.append(26)
lista.append (57)
lista.append (900)
print(lista)
valor_do_pop = lista.pop( )
print(lista)
print(f' foi removido da lista o cliente de id: {valor_do_pop}')
lista.insert(0, 'Amontada Valley')
print(lista)
lista.insert(2, 'Professor')
print(lista)
lista.insert(200, 'Professor')
print(lista)