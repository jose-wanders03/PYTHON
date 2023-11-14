# Inicializar uma lista para armazenar as médias dos alunos
medias_alunos = []

# Loop para obter notas de quatro alunos
for i in range(4):
    notas = [float(input(f"Informe a nota {j + 1} do aluno {i + 1}: ")) for j in range(3)]
    
# Calcular a média das notas do aluno
media_aluno = sum(notas) / len(notas)
    
# Adicionar a média à lista
medias_alunos.append(media_aluno)

# Imprimir as médias dos alunos
print("Médias dos alunos:", medias_alunos)