# Lista de listas (mapa) 🗺️
# python
# mapa = [
#     [".", "M", "."],
#     ["M", ".", "."],
#     [".", ".", "X"],
#     [".", "M", "."]
# ]

# Escreva contarMonstros(mapa) que devolve quantos "M" existem e acharTesouro(mapa) que devolve linha e coluna do "X" (ou None, None).
# Dois for aninhados, com len(mapa[linha]) no de dentro. Mostre Há 4 monstros e Tesouro na linha 2 e coluna 2.

mapa = [
    [".", "M", "."],
    ["M", ".", "."],
    [".", ".", "X"],
    [".", "M", "."]
]

def contarMonstros(mapa):
    monstros = 0
    for linhas in range(len(mapa)):
        for colunas in mapa[linhas]:
            if colunas == "M":
                monstros += 1
    return monstros

def acharTesouro(mapa):
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            if mapa[linha][coluna] == "X":
                return linha, coluna
    return None, None


totalMonstros = contarMonstros(mapa)
print(f"Há {totalMonstros} monstros")

linhaTesouro, colunaTesouro = acharTesouro(mapa)
print(f"Tesouro na linha {linhaTesouro} e coluna {colunaTesouro}")


# Dicionário + “Na Main” 🎓
# python
# monstros = [
#     {"nome": "Slime", "vida": 30},
#     {"nome": "Goblin", "vida": 55},
#     {"nome": "Morcego", "vida": 15}
# ]
# inventario = {"pocao": 2, "flecha": 20}

# Faça três funções:

# somaVida(monstros): devolve a soma das vidas.
# maisFraco(monstros): devolve nome e vida do mais fraco.
# usarItem(inventario, nomeItem): devolve True (diminuindo 1) se o item existe e a quantidade é maior que 0, senão False.

# Na main(), mostre:

# Vida total: 100
# O mais fraco é Morcego com 15 de vida
# Usou pocao: True
# Usou espada: False

def somaVida(monstros):
    vidaTotal = 0
    for monstro in monstros:
        vidaTotal += monstro["vida"]
    return vidaTotal

def maisFraco(monstros):
    menorVida = None
    nomeMaisFraco = ""
    for monstro in monstros:
        if menorVida == None:
            menorVida = monstro["vida"]
            nomeMaisFraco = monstro["nome"]
        if menorVida > monstro["vida"]:
            menorVida = monstro["vida"]
            nomeMaisFraco = monstro["nome"]
    return nomeMaisFraco, menorVida

def usarItem(inventario, nomeItem):
    if nomeItem in inventario and inventario[nomeItem] > 0:
        inventario[nomeItem] -= 1
        return True
    return False

def main():
    monstros = [
        {"nome": "Slime", "vida": 30},
        {"nome": "Goblin", "vida": 55},
        {"nome": "Morcego", "vida": 15}
    ]
    inventario = {"pocao": 2, "flecha": 20}

    vidaTotal = somaVida(monstros)
    print(f"Vida total: {vidaTotal}")

    nome, vida = maisFraco(monstros)
    print(f"O mais fraco é {nome} com {vida} de vida")

    resultado = usarItem(inventario, "pocao")
    print(f"Usou pocao: {resultado}")

    resultado = usarItem(inventario, "espada")
    print(f"Usou espada: {resultado}")

main()