# Ficha do herói 🧙

# Crie um dicionário heroi com estas informações:

# "nome": "Ana"
# "vida": 100
# "ouro": 30

# Depois:

# Mostre a vida do herói acessando pela chave.
# O herói recebeu um golpe: diminua 25 da vida.
# O herói achou um baú: aumente 50 no ouro.
# Adicione uma chave nova "nivel" com valor 1.
# Mostre o dicionário final com print(heroi).

# Saída esperada:

# 100
# {'nome': 'Ana', 'vida': 75, 'ouro': 80, 'nivel': 1}

heroi = {"nome": "Ana", "vida": 100, "ouro": 30}

print(heroi["vida"])
heroi["vida"] -= 25
heroi["ouro"] += 50
heroi["nivel"] = 1
print(heroi)


# Conferindo a ficha 📜

# Usando o mesmo heroi, percorra-o com for chave, valor in heroi.items(): e mostre uma linha por informação:

# nome: Ana
# vida: 75
# ouro: 80
# nivel: 1

# Depois, use if/else com in para checar se existe a chave "armadura" e mostre "Herói sem armadura" ou "Herói com armadura".

for chave, valor in heroi.items():
    print(f"{chave}: {valor}")
if "armadura" in heroi:
    print("Herói com armadura")
else:
    print("Herói sem armadura")