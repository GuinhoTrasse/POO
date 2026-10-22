# Função com return 💀
# python
# danos = [20, 35, 50]

# Escreva somaDanos(danos) que devolve a soma. Fora dela, mostre Game over! se o total for >= 100, senão Sobreviveu!.

danos = [20, 35, 50]

def somaDanos(danos):
    soma = 0
    for dano in danos:
        soma += dano
    return soma

soma = somaDanos(danos)
if soma >= 100:
    print("Game over!")
else:
    print("Sobreviveu!")


# Recorde com dois valores 🏆
# python
# jogadores = ["Ana", "Bruno", "Carla"]
# pontos = [1200, 3400, 2800]

# Escreva campeao(jogadores, pontos) que devolve nome e pontos do maior (recorde começando com None, for com range(len(...))). Mostre O campeão é Bruno com 3400 pontos.

jogadores = ["Ana", "Bruno", "Carla"]
pontos = [1200, 3400, 2800]

def campeao(jogadores, pontos):
    recorde = None
    melhorJogador = ""
    for posicao in range(len(jogadores)):
        if recorde == None:
            recorde = pontos[posicao]
            melhorJogador = jogadores[posicao]
        if recorde < pontos[posicao]:
            recorde = pontos[posicao]
            melhorJogador = jogadores[posicao]
    return melhorJogador, recorde

melhorJogador, recorde = campeao(jogadores, pontos)
print(f"O campeão é {melhorJogador} com {recorde} pontos")