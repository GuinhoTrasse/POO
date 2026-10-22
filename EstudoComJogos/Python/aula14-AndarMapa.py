# Andando no mapa 🧭

# Agora o mapa tem "H" (herói) e "." (chão):

# python
# mapa = [
#     [".", ".", "."],
#     [".", "H", "."],
#     [".", ".", "."]
# ]

# Escreva uma função moverHeroi(mapa, linhaAtual, colunaAtual) que move o herói uma casa para a direita:

# Coloque "." na posição atual.
# Coloque "H" na casa à direita (colunaAtual + 1).
# Devolva a nova linha e a nova coluna.

# Fora da função, comece com o herói na linha 1 e coluna 1, chame a função, guarde o retorno desempacotando, e mostre o mapa linha por linha com um for:

# ['.', '.', '.']
# ['.', '.', 'H']
# ['.', '.', '.']

# Atenção: o mapa é lista, então a função altera o de fora direto (como no usarItem), e aqui a atribuição usa =, não ==: mapa[linha][coluna] = ".".

mapa = [
    [".", ".", "."],
    [".", "H", "."],
    [".", ".", "."]
]

def moverHeroi(mapa, linhaAtual, colunaAtual):
    mapa[linhaAtual][colunaAtual] = "."
    colunaAtual += 1
    mapa[linhaAtual][colunaAtual] = "H"
    return linhaAtual, colunaAtual

novaLinha, novaColuna = moverHeroi(mapa, 1, 1)

for linha in mapa:
    print(linha)


# Herói que anda até a parede 🧱

# Usando a mesma ideia, escreva andarAteParede(mapa, linha, coluna), que move o herói para a direita, uma casa por vez, até chegar na última coluna do mapa, e devolve a posição final.
# Use um while (ou um for com range, como preferir), lembrando de apagar o “H” antigo a cada passo.

# Mapa de teste:

# python
# mapa = [
#     ["H", ".", ".", "."],
#     [".", ".", ".", "."]
# ]

# Fora da função, chame com linha 0 e coluna 0, desempacote e mostre:

# ['.', '.', '.', 'H']
# ['.', '.', '.', '.']
# O herói parou na linha 0 e coluna 3

# Dica de caminho: pense em quantos passos faltam (len(mapa[linha]) - 1 - coluna). Se preferir não usar while, um for com range desse número de passos resolve.