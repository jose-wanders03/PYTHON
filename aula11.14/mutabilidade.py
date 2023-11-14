# Alguns cuidados com dados mutaveis
# Mutaveis - são dados que podem ter seu valor alterado na memoria do dispositivo
# Imuntaveis - são dados que so podem ser copiados da memoria do dispositivo

lista = ['João', 'Wanderson']
lista [1] = 'José'
print(lista)

nome = 'Wanderson' 
# nome = 'João'
# nome[2] = 'a'
novo_nome = nome  
nome = 'João'
print(nome)
print(novo_nome)


lista_a = ['João', 'Paulo']
lista_b = lista_a.copy()
lista_c = lista_b
lista_c[1] = 'Jose'
print(lista_a)
print(lista_b)
print(lista_c)