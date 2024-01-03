'''class Estudante:
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula
        self.nome_classe = self.__class__.__name__
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    cpf = property(get_cpf, set_cpf)

class EstudanteGraduacao(Estudante):
    def __init__(self, curso, nome, matricula):
        self.curso = curso
        super().__init__(nome, matricula)
        
    
    def __str__(self):
        return f'A sua classe é { self.nome_classe }. Olá, { self._nome } seu CPF é: { self.get_cpf() } seu curso de Graduação é o de { self.curso } e sua matricula de acesso é { self._matricula }'

class EstudantePos(Estudante):
    nivel = 1
    orientador = 'Prof Carlos Alberto'

    def __str__(self):
        return f'A sua classe é { self.nome_classe }.Olá, { self._nome } seu nivel é { self.nivel }° e seu Tutor será o { self.orientador }. para seu acesso utilize a matricula { self._matricula }'

aluno1 = EstudanteGraduacao('ADS', 'Paulo Junior', 353637)
# aluno2 = EstudantePos('Paulo Junior', '565758')


aluno1.set_cpf(123456789)
print(aluno1.get_cpf())
print(aluno1)
# print(aluno2)'''


'''contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 2
    if(contador == 5):
        contador = contador + 2'''

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo")