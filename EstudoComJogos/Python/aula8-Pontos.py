# Quem é o último? 🥉

# Usando as mesmas listas jogadores e pontos, descubra quem fez menos pontos (o recorde de menor) e mostre: O último colocado é Ana com 1200 pontos.

# Dica de caminho: é o mesmo padrão do exercício 12, só muda a direção da comparação.

jogadores = ["Ana", "Bruno", "Carla", "Davi"]
pontos = [1200, 3400, 2800, 3100]

menorPontuacao = None
piorJogador = ""

for posicao in range(len(pontos)):
    if menorPontuacao == None:
        menorPontuacao = pontos[posicao]
        piorJogador = jogadores[posicao]
    if menorPontuacao > pontos[posicao]:
        menorPontuacao = pontos[posicao]
        piorJogador = jogadores[posicao]
print(f"O último colocado é {piorJogador} com {menorPontuacao} pontos")