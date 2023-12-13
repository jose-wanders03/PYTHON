# 1. crie uma lista de alunos com nome e nota final de cada aluno e coloque em um dicionario, depois imprima

'''lista_de_alunos = [['Pedro' 5] , ['Thiago' 6] , ['João' 8] , ['Rafael', 10]]
dic = {}
dic.update(lista_de_alunos)
print(dic)'''

# Ainda sobre a questão 1. Inserir mais 04 alunos e notas no seu dicionario



# Faça um código que pede a marca e o modelo do carro do cliente, insira ele em uma lista e depois transforme em um dicionario. Imprima os dois

'''lista_de_carros = []
marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
lista_de_carros.append({marca})
lista_de_carros.append({modelo})

dic_carros = {}
dic_carros.update([lista_de_carros])

print(lista_de_carros)
print(dic_carros)

dic_carros['Fiat'] = 'Uno'
print(dic_carros)'''



# 4 crie um cadastro de clientes recebendo nome, idade, data de aniversário e endereço completo.  Adicione todas às informações em um dicionario. Imprima ao final.
'''dic = {'nome': 'Wanderson'}    
dic.update({'idade': 20 })
dic.update(aniversario = '14/06/2003')
dic.update(endereco = 'Pv de Gostosa, Zona Rual, s/n, Amontada-Ce') 
print(dic)'''



# 5 Vamos criar um sistema de login e senha. Crie um dicionario contendo os acessos dos colaboradores com o nome de usuario e senha, em seguida peça as informações e valide o login do usuario.

'''lista_de_usuario = {}

usuario =input("Digite nome de usuario: ")
senha = int(input("Digite sua senha: "))
    
for i in range(4):'''



# 6. Faça um quizz utilizando um dicionario com as seguintes chaves: Pergunta, opções e resposta. Faça a validação da opção escolhida com a resposta e imprima
pergunta = [
           {"Pergunta": " Qual a capital do Ceará?",
            "Opções": ["a) Florianopolis", "b) Rio de Janeiro", "c) Brasília", "d) Fortaleza"],
            "Resposta": "d"},

            {"Pergunta": " Qual o maior estado brasileiro?",
            "Opções": ["a) Amazonas", "b) Uruguai", "c) Brasília", "d) Fortaleza"],
            "Resposta": "a"},

            {"Pergunta": "Em qual região do Brasil está localizado o Maranhão?",
            "Opções": ["a) Sul", "b) Nordeste", "c) Noroeste", "d) Sudeste"],
            "Resposta": "b"},

            {"Pergunta": "Em qual cidade do Ceará está localizada a estátua de Padre Cícero?",
            "Opções": ["a) Juazeiro do Norte", "b) Sobral", "c) Itapipoca", "d) Fortaleza"],
            "Resposta": "a"},

            {"Pergunta": " Qual dos estados abaixo faz parte da região norte do Brasil?",
            "Opções": ["a)Brasília ", "b) Rio de Janeiro", "c) Pará", "d) Fortaleza"],
            "Resposta": "c"},
]

for pergunta in pergunta:
    print('pergunta:', pergunta['pergunta'])
    print()

    for i, opcao in enumerate(pergunta["Opções"]):
        print(f'{i+1})', opcao)
        print()
   

resposta_escolhida = int(input("Escolha a opção correta: "))
acertou = False

if resposta_escolhida == int(pergunta['Resposta'])
acertou = True    
print()

if acertou:
    print("Parabéns! Você acertou!")
else:
    print(f"Ops! A resposta correta era {pergunta['Resposta']}. Tente novamente.")





# MATRIZES PYTHON

'''matriz =[[1],[2],[3],
         [4],[5],[6],
         [7],[8],[9],
]

print(matriz[4][0])'''






