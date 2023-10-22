def peso_ideal(h, genero):
    if genero == "homem":
        peso = (72.7 * h) - 58
    elif genero == "mulher":
        peso = (62.1 * h) - 44.7
    else:
        return "Gênero inválido"
    return f"Seu peso ideal é de aproximadamente {peso:.2f} kg."

# Exemplo de uso:
print(peso_ideal(1.75, "homem"))