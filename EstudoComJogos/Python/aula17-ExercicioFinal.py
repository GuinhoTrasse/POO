# formato de faculdade 🎓

# Como a prova é amanhã, aqui vai um no estilo “Na Main”, juntando o que você viu (lista de dicionários, funções, vários retornos).

# Arena dos monstros. Cada monstro é um dicionário com nome e vida:

# python
# monstros = [
#     {"nome": "Slime", "vida": 30},
#     {"nome": "Goblin", "vida": 55},
#     {"nome": "Orc", "vida": 80},
#     {"nome": "Morcego", "vida": 15}
# ]

# Faça duas funções:

# somaVida(monstros): devolve a soma da vida de todos os monstros.
# maisFraco(monstros): devolve o nome e a vida do monstro com menos vida.

# Na Main, chame as duas funções e mostre:

# Vida total: 180
# O mais fraco é Morcego com 15 de vida

# Lembretes: contador começa em 0 antes do for; recorde começa em None (e a comparação vai na direção do menor);
# return fora do for; desempacote o retorno de maisFraco na mesma ordem em que ele devolve.

def somaVida(monstros):
    vidaTotal = 0
    for monstro in monstros:
        vidaTotal += monstro["vida"]
    return vidaTotal

def maisFraco(monstros):
    menorVida = None
    nomeMonstro = None
    for monstro in monstros:
        if menorVida == None:
            nomeMonstro = monstro["nome"]
            menorVida = monstro["vida"]
        if menorVida > monstro["vida"]:
            nomeMonstro = monstro["nome"]
            menorVida = monstro["vida"]
    return nomeMonstro, menorVida

def main():
    monstros = [
        {"nome": "Slime", "vida": 30},
        {"nome": "Goblin", "vida": 55},
        {"nome": "Orc", "vida": 80},
        {"nome": "Morcego", "vida": 15}
    ]

    vidaTotal = somaVida(monstros)
    print(f"Vida total: {vidaTotal}")

    nome, vida = maisFraco(monstros)
    print(f"O mais fraco é {nome} com {vida} de vida")

main()