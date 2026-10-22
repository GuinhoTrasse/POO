# Tupla 📍
# python
# posicao = (3, 5)

# Escreva andar(posicao, direcao) que devolve uma nova tupla ("direita": x+1, "esquerda": x-1, "cima": y-1, "baixo": y+1).
# Fora da função, ande "direita" e depois "baixo", guardando o retorno, e mostre Posição: (4, 6).

def andar(posicao, direcao):
    x, y = posicao
    if direcao == "direita":
        x += 1
    elif direcao == "esquerda":
        x -= 1
    elif direcao == "cima":
        y -= 1
    elif direcao == "baixo":
        y += 1
    return x, y

posicao = (3, 5)

novaPosicao = andar(posicao, "direita")
novaPosicao = andar(novaPosicao, "baixo")
print(f"Posição: {novaPosicao}")

# Lista de tuplas 🛒
# python
# loja = [("espada", 150), ("escudo", 90), ("pocao", 25)]

# Com for nome, preco in loja:, mostre só os itens com preço menor que 100: escudo custa 90 moedas e pocao custa 25 moedas.

loja = [("espada", 150), ("escudo", 90), ("pocao", 25)]

for nome, preco in loja:
    if preco < 100:
        print(f"{nome} custa {preco} moedas")