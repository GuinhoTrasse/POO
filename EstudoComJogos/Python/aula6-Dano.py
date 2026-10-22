# Maior dano ⚔️

# Escreva uma função maiorDano(listaDanos) que recebe uma lista de danos e devolve o maior valor dela (o recorde, que você já domina). Teste com:

# python
# danosChefe = [12, 47, 8, 33, 29]

# Mostre fora da função: O golpe mais forte causou 47 de dano.

danosChefe = [12, 47, 8, 33, 29]
def maiorDano(listaDanos):
    danoForte = None
    for dano in listaDanos:
        if danoForte == None:
            danoForte = dano
        if dano > danoForte:
            danoForte = dano
    return danoForte

danoGrande = maiorDano(danosChefe)
print(f"O golpe mais forte causou {danoGrande} de dano")


# Ranking de pontos 🏆

# Dois jogadores têm suas pontuações em listas separadas, com a mesma posição para cada pessoa:

# python
# jogadores = ["Ana", "Bruno", "Carla", "Davi"]
# pontos = [1200, 3400, 2800, 3100]

# Descubra quem fez mais pontos e mostre: O campeão é Bruno com 3400 pontos.

# Dica de caminho: junte o que você aprendeu no exercício 10 (usar a posição nas duas listas) com a lógica de recorde. Guarde a posição do maior, não só o valor.

jogadores = ["Ana", "Bruno", "Carla", "Davi"]
pontos = [1200, 3400, 2800, 3100]
maiorPonto = None
melhorJogador = ""
for posicao in range(len(pontos)):
    print(f"jogador: {jogadores[posicao]} - {pontos[posicao]}")
    if maiorPonto == None:
        maiorPonto = pontos[posicao]
        melhorJogador = jogadores[posicao]
    if pontos[posicao] > maiorPonto:
        maiorPonto = pontos[posicao]
        melhorJogador = jogadores[posicao]
print(f"O campeão é {melhorJogador} com {maiorPonto} pontos.")