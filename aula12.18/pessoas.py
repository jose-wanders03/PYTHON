
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        self.__cpf = None
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade} e CPF: {self.__cpf}'
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf


class Professor(Pessoa):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina
        


class Aluno(Pessoa):
    pass

Wanderson = Professor('Wanderson', 20 , 2230.00, 'Ensino Médio', )
Wanderson.set_cpf(15269186217)
print(Wanderson)
