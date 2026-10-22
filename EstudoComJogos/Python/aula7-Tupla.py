# Primeira tupla 📍

# Uma tupla é como uma lista que não pode ser alterada depois de criada. Ela usa parênteses. A posição do herói no mapa é guardada assim:

# python
# posicaoHeroi = (3, 5)

# O primeiro número é a coluna (x) e o segundo é a linha (y). Faça um programa que:

# Mostre a posição completa.
# Mostre só o x e só o y, acessando pelo índice, como na lista.
# Desempacote a tupla em duas variáveis (x, y = posicaoHeroi) e mostre: O herói está na coluna 3 e na linha 5.
# Tente fazer posicaoHeroi[0] = 10 e veja o que acontece. Depois me diga com suas palavras o que o Python respondeu e por quê.

posicaoHeroi = (3, 5)
print(posicaoHeroi)

coluna = posicaoHeroi[0]
linha = posicaoHeroi[1]
print(posicaoHeroi[0])
print(posicaoHeroi[1])

coluna, linha = posicaoHeroi
print(f"O herói está na coluna {coluna} e na linha {linha}")

# posicaoHeroi[0] = 10
# o que o pyton escreveu:
#  File "d:\Documents\EstudoComJogos\aula7-Tupla.py", line 26, in <module>
#     posicaoHeroi[0] = 10
#     ~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# ele escreveu isso pois não é possível alterar o valor da tupla
