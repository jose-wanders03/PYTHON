# possuem CHAVE(KEYS) e VALOR(VALLUES)
# paremetro: () ou dict()

'''
pessoa = { 'nome': 'Paulo',
          'sobrenome ': 'Junior1'
        'nome 2'    :     'Rodrigo'
          'sobrenome ': 'Junior2
          'sobrenome 4':   'junior' }
 
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())

k = pessoa.keys()
k = pessoa.values()

for chave in pessoa:
    print(chave)

for valor in v:
    print(valor)

print("="*20)

for valor in pessoa.values():
    print(chave)

for chave, valor in pessoa.items( ):
    print(chave, valor)                                

i = pessoa.items(
    print(i))


print("="*20)

print(pessoa['sobrenome2 '])
print('sobrenome')'''




d1 = {'valor1': 100,
       'valor2': 200,
       'valor3': 300, }


d2 = d1

print(d1)


d2['valor2'] = 'Wanderson'

print(d1)

print((d2))

print(d2.get('valor2'))

d3 = d1.pop('valor3')
print(d1)

outro_nome = {'valor5': 5,
              'valor6': 6}

d1.update(outro_nome)

print(d1)

print(d1.has_key('valor1'))