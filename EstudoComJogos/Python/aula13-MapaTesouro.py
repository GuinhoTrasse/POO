# Mapa do tesouro 🗺️

# O mapa é uma lista de listas (cada lista interna é uma linha). "." é chão, "X" é o tesouro:

# python
# mapa = [
#     [".", ".", "."],
#     [".", ".", "X"],
#     [".", ".", "."]
# ]

# Escreva uma função acharTesouro(mapa) que percorre o mapa com dois for aninhados (um para as linhas, outro para as colunas, usando range(len(...)))
# e devolve duas posições: a linha e a coluna do "X". Se não houver "X", devolve None, None.

# Fora da função, desempacote e mostre:

# Tesouro na linha 1 e coluna 2

# Lembretes do seu histórico: nos range, as variáveis guardam posições, e o valor é mapa[linha][coluna].
# O return com a posição pode ficar dentro dos loops (achou, devolve), mas o return None, None fica fora de ambos.

mapa = [
    [".", ".", "."],
    [".", ".", "X"],
    [".", ".", "."]
]

def acharTesouro(mapa):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            if mapa[linha][coluna] == "X":
                return linha, coluna
    return None, None

tesouro = acharTesouro(mapa)
linha, coluna = tesouro
print(f"Tesouro na linha {linha} e coluna {coluna}")

# Contando monstros 👹

# No mapa, "M" é monstro e "." é chão:

# python
# mapa = [
#     ["M", ".", "."],
#     [".", "M", "."],
#     [".", ".", "M"],
#     [".", ".", "."]
# ]

# Escreva uma função contarMonstros(mapa) que devolve quantos "M" existem no mapa, usando dois for aninhados. Fora da função, mostre:

# Há 3 monstros no mapa

# Atenção: o contador começa em 0 antes dos loops, e o return fica fora dos dois for. Aqui o mapa tem 4 linhas e 3 colunas, então use len(mapa[linha]) no loop de dentro.

mapa = [
    ["M", ".", "."],
    [".", "M", "."],
    [".", ".", "M"],
    [".", ".", "."]
]

def contarMonstros(mapa):
    monstros = 0
    for linha in range(len(mapa)):
        for coluna in range (len(mapa[linha])):
            if mapa[linha][coluna] == "M":
                monstros += 1
    return monstros

totalmonstros = contarMonstros(mapa)
print(f"Há {totalmonstros} monstros no mapa")