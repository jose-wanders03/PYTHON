# Crie uma classe base chamada Animal com métodos comer() e dormir(). Em seguida, crie duas classes derivadas chamadas Cachorro e Gato que herdam de Animal. Adicione um método específico para cada classe derivada, como latir() para o Cachorro e miar() para o Gato.

'''class Animal:
    def comer(self):
        print("Animal comendo.")

    def dormir(self):
        print("Animal dormindo.")

class Cachorro(Animal):
    def latir(self):
        print("Au Au")

class Gato(Animal):
    def miar(self):
        print("Miau")

# Testando herança
cachorro = Cachorro()
gato = Gato()

cachorro.comer()
cachorro.dormir()
cachorro.latir()

gato.comer()
gato.dormir()
gato.miar()'''


# Crie uma classe base chamada Pessoa com um método apresentar() que imprime "Eu sou uma pessoa.". Em seguida, crie uma classe derivada chamada Estudante que herda de Pessoa e sobrescreve o método apresentar() para imprimir "Eu sou um estudante.".


'''class Pessoa:
    def apresentar(self):
        print("Eu sou uma pessoa.")

class Estudante(Pessoa):
    def apresentar(self):
        print("Eu sou um estudante.")

# Testando herança e sobrescrita de métodos
pessoa = Pessoa()
estudante = Estudante()

pessoa.apresentar()
estudante.apresentar()'''



# Criar uma Class televisão

