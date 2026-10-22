# Lista básica 🎒
# python
# mochila = ["espada", "mapa", "tocha"]

# Adicione "escudo" no final, troque a posição 0 por "machado", remova "mapa" e mostre a lista e a quantidade de itens.

# Saída esperada:

# ['machado', 'tocha', 'escudo']
# 3

mochila = ["espada", "mapa", "tocha"]

mochila.append("escudo")
mochila[0] = "machado"
mochila.remove("mapa")
print(mochila)
print(len(mochila))

# for com if 🧪
# python
# loot = ["gema", "pele", "gema", "anel", "gema"]

# Conte quantas "gema" existem e mostre Há 3 gemas.

loot = ["gema", "pele", "gema", "anel", "gema"]
gema = 0
for item in loot:
    if item == "gema":
        gema+=1

print(f"Há {gema} gemas")