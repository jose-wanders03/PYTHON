class automovel:
    def __init__(self, placa ='XYZ-4925'):
       self.placa = placa
    def get_placa(self):
       return self.placa  
    def dirigir(self, velocidade):
       print(f'Estou dirigindo a { velocidade} Km/h')

carro = automovel()
print(carro.get_placa())
carro.dirigir(220) 