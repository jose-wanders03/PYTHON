class ContaBancaria:
    def __init__(self):
        self.__saldo = 0
        self.__titular = ""

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def get_titular(self):
        return self.__titular

    def set_titular(self, novo_titular):
        self.__titular = novo_titular

# Testando get e set em uma conta bancária
conta = ContaBancaria()

conta.set_titular("João")
conta.set_saldo(1000)

print(f"Titular: {conta.get_titular()}")
print(f"Saldo: {conta.get_saldo()}")


# Crie uma classe chamada Carro com os atributos privados modelo, ano e quilometragem. Implemente métodos de acesso (get e set) para cada um dos atributos. Utilize os métodos set para validar que o ano seja um valor positivo e a quilometragem seja um valor não negativo. Demonstre a utilização desses métodos em um objeto da classe.

class Carro:
    def __init__(self):
        self.__modelo = ""
        self.__ano = 0
        self.__quilometragem = 0

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, novo_modelo):
        if isinstance(novo_modelo, str) and novo_modelo.strip() != "":
            self.__modelo = novo_modelo
        else:
            print("Erro: Modelo deve ser uma string não vazia.")

    def get_ano(self):
        return self.__ano

    def set_ano(self, novo_ano):
        if novo_ano > 0:
            self.__ano = novo_ano
        else:
            print("Erro: Ano deve ser um valor positivo.")

    def get_quilometragem(self):
        return self.__quilometragem

    def set_quilometragem(self, nova_quilometragem):
        if nova_quilometragem >= 0:
            self.__quilometragem = nova_quilometragem
        else:
            print("Erro: Quilometragem deve ser um valor não negativo.")

# Testando get e set em um objeto Carro
carro = Carro()

carro.set_modelo("Fusca")
carro.set_ano(1975)
carro.set_quilometragem(150000)

print(f"Modelo: {carro.get_modelo()}")
print(f"Ano: {carro.get_ano()}")
print(f"Quilometragem: {carro.get_quilometragem()} km")