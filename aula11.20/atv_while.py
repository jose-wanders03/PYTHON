# Faça um codigo que peça uma nota, entre zero e dez. Mostre uma mensagem caso a nota seja inválida e continue pedindo até que o usuário informe uma nota válida.

'''while True:
    nota = float(input(f'Digite uma nota entre 0 e 10:'))
    print('Nota Válida!')'''



# Faça um codigo que leia um nome de usuário e sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e pedindo as informações novamente.

'''while True:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario == senha:
        print("Erro! A senha não pode ser igual ao nome do usuário. Faça uma nova tentativa.")
    else:
        print("Login aceito")
        break'''
    

# Faça um codigo que leia 5 numeros e informe o maior numero

# Loop para ler 5 números
for i in range(5):
    # Lê o número do usuário
    numero = float(input(f"Digite o {i + 1}º número: "))
    
    # Verifica se é o maior número até agora
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

# Exibe o maior número
print(f"O maior número é: {maior_numero}")
    



    