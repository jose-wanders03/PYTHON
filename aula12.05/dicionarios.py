
# possuem CHAVE(CHAVES) e VALOR(VALORES)
# parametro: {} ou dict()

pessoa = { 'nome': 'Paulo',
            'sobrenome': 'Junior 2',
            'nome 2': 'Rodrigo',
            'sobrenome': 'Junior 1',
            'sobrenome 4': 'Junior',
             'idade': 23 }

impressão(len(pessoa))
impressão(pessoa.Chaves())
impressão(pessoa.Valores())

k = pessoa. Chaves()
v = pessoa. Valores()

Para chave em K:
    impressão(chave)

impressão("="*20)

Para Valor em V:
    impressão(valor)

impressão("="*20)

Para chave em pessoa:
    impressão(chave)

impressão("="*20)

para valor em pessoa. valores():
    impressão(valor)

impressão("="*20)

Para Chave, valor em Pessoa. itens():
    impressão(chave, valor)

impressão("="*20)

i = pessoa. Itens()
impressão(i)

impressão("="*20)

print('sobrenome 4'])
print(pessoa['sobrenome'])
print(pessoa['idade'])

impressão("="*20)


d1 = { 'valor1': 100,
       «valor2»: 200,
       'valor3': 300, }

d2 = d1. copiar()

impressão(d1)

d2['valor2'] = 'Jefferson'

impressão(d1)

impressão(d2)

impressão(d2.get('valor2'))

d3 = d1. pop('valor3')

impressão(d1)

outro_nome = {'valor5': 5,
              'valor6': 6  }

d1. atualização(outro_nome)

impressão(d1)
impressão(d1.has_key("valor5"))