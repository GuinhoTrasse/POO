# mochila = ["espada", "pocao", "mapa"]

# Faça um programa que:

# Mostre a mochila completa na tela.
# Mostre apenas o primeiro item da mochila.
# Mostre apenas o último item da mochila.

mochila = ["espada", "pocao", "mapa"]

print(mochila)
print(mochila[0])
print(mochila[-1])

# Achou um tesouro! 💰

# Continuando a aventura com a mesma mochila, você encontra um baú e precisa mexer no inventário:

# Adicione o item "escudo" no final da mochila.
# Remova a "pocao" (você bebeu ela numa batalha).
# Mostre a mochila final na tela.

mochila.append("escudo")
mochila.remove("pocao")
print(mochila)