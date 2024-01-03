# Crie abstração para uma super classe funcionario com duas subclasses.


class Empresa:
    def __init__(self, nome, idade, jornada_de_trabalho, salario, função):
        self.nome = nome 
        self.idade = idade
        self.salario = salario
        self.função = função
        return f' Tenho um sálario de: {self.salario}, minha função é : {self.função} '


class Funcionarios(Empresa):
        pass
    
    
    

pessoa = Funcionarios()
print(f'Meu nome é {empresa.nome}, tenho {empresa.idade}, recebo um salário de {empresa.salario} sendo {empresa.Contador}')





        
    
    


    

        
        
    

