# Crie uma classe chamada Pessoa com os atributos nome e idade. Instancie dois objetos dessa classe e imprima suas informações.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Instanciando objetos
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

# Imprimindo informações
print(f"{pessoa1.nome} tem {pessoa1.idade} anos.")
print(f"{pessoa2.nome} tem {pessoa2.idade} anos.")



# Crie uma classe base chamada Veiculo com um método ligar() e uma classe derivada chamada Carro que herda de Veiculo. Adicione um método adicional à classe Carro chamado acelerar().

class Veiculo:
    def ligar(self):
        print("Veículo ligado.")

class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando.")

# Testando a herança
carro = Carro()
carro.ligar()
carro.acelerar()


# Crie uma classe Animal com um método fazer_som(). Em seguida, crie classes derivadas Cachorro e Gato que sobrescrevem o método fazer_som(). Demonstre o polimorfismo chamando o método em objetos das duas classes.

class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au")

class Gato(Animal):
    def fazer_som(self):
        print("Miau")

# Testando polimorfismo
animal1 = Cachorro()
animal2 = Gato()



