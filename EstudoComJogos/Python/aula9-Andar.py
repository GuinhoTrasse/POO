# O herói anda 🚶

# O herói está em posicaoHeroi = (3, 5). Escreva uma função andar(posicao, direcao) que recebe a posição (tupla) e uma direção (texto) e devolve uma nova tupla com a posição depois
# de um passo:

# "direita": x aumenta 1
# "esquerda": x diminui 1
# "cima": y diminui 1
# "baixo": y aumenta 1

# Fora da função, teste com "direita" e depois com "cima", guardando o resultado e mostrando:

# O herói está na coluna 4 e na linha 5
# O herói está na coluna 4 e na linha 4

# Dicas: use o desempacotamento dentro da função para separar x e y, e lembre que o return fica fora de qualquer loop. Aqui nem precisa de loop, só de if/elif.


def andar(posicao, direcao):
    x, y = posicao
    if direcao == "direita":
        x += 1
    elif direcao == "esquerda":
        x -= 1
    elif direcao == "baixo":
        y += 1
    elif direcao == "cima":
        y -= 1
    return x, y

posicaoHeroi = (3, 5)

posicaoHeroi = andar(posicaoHeroi, "direita")
x, y = posicaoHeroi
print(f"O herói está na coluna {x} e na linha {y}")

posicaoHeroi = andar(posicaoHeroi, "cima")
x, y = posicaoHeroi
print(f"O herói está na coluna {x} e na linha {y}")