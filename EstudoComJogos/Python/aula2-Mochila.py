# Trocou de arma ⚔️

# Sua mochila agora é:

# python
# mochila = ["espada", "escudo", "mapa", "tocha"]

# Você encontrou um machado lendário e quer trocar a espada por ele.

# Substitua o item da posição 0 por "machado".
# Mostre quantos itens tem na mochila (dica de busca: a função len).
# Mostre a mochila final.

mochila = ["espada", "escudo", "mapa", "tocha"]

# da pra fazer assim, mas n é recomendado
# del mochila[0] 
# mochila.insert(0, "machado")

# o jeito certo:
mochila[0] = "machado"
print(f"A mochila contém {len(mochila)} itens")
print(f"Mochila: {mochila}")

# Inspeção da mochila 🔦

# Usando a mesma mochila do exercício 3 (já com o machado), faça um programa que percorra a mochila com for e mostre cada item em uma linha, assim:

# Item: machado
# Item: escudo
# Item: mapa
# Item: tocha

for item in mochila:
    print(f"Item: {item}")