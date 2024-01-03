from logging import captureWarnings
from traceback import format_exc


class Pet:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.fome = 0
        self.sede = 0
        self.comida = 100
    
    # Os GETs
    def get_nome(self):
        return self.nome
    
    def gt_peso(self):
        return self.peso
    
    def gt_fome(self):
        return self.fome
   
    
    # Os SETs

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_peso(self, novo_peso):
        self.peso = novo_peso
    
    def set_fome(self, nova_fome):
        self.fome = nova_fome
        if self.fome >= 99:
            print(f'Alimente a/o {self.nome}')
            nova_comida = int(input('Quanto de comida você quer dar para seu Pet? '))
            self.comida -= nova_comida
            self.fome -= nova_fome

    
    
    def imprimir(self):
        print(f'Olá, me chamo {self.nome}')
        print(f'Estou pesando {self.peso} kg')
        print(f'Minha fome está em {self.fome}')
        print(f'Minha sede está {self.sede}')

caozinho = Pet('Totó', 20)
caozinho.imprimir()

caozinho.set_fome(15)
caozinho.imprimir()
caozinho.set_fome(20)
caozinho.imprimir()
caozinho.set_fome(30)
caozinho.imprimir()
caozinho.set_fome(70)
caozinho.imprimir()
caozinho.set_fome(10)
caozinho.imprimir()

