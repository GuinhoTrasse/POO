# Mochila com quantidade 🎒

# Agora a mochila é uma lista de listas, e cada item é [nome, quantidade]. Uso lista (e não tupla) porque a quantidade vai mudar:

# python
# mochila = [["pocao", 3], ["flecha", 20], ["tocha", 1]]

# Faça um programa que:

# Percorra a mochila com for item in mochila: e mostre, por exemplo, pocao: 3 (aqui item guarda a lista inteira ["pocao", 3], então use item[0] e item[1]).
# Depois, o herói bebe uma poção: ache a "pocao" na mochila e diminua 1 da quantidade dela (atribuindo com -= na posição certa).
# Mostre a mochila final com print(mochila).

# Saída esperada:

# pocao: 3
# flecha: 20
# tocha: 1
# [['pocao', 2], ['flecha', 20], ['tocha', 1]]

# Atenção ao seu ponto de atenção: dentro do for, item é a lista inteira, item[0] é o nome e item[1] é a quantidade.

mochila = [["pocao", 3], ["flecha", 20], ["tocha", 1]]

for item in mochila:
    print(f"{item[0]}: {item[1]}")

for item in mochila:
    if item[0] == "pocao":
        if item[1] > 0:
            print("Herói bebe uma poção em meio a batalha!")
            item[1] -= 1

print(mochila)


# Função que usa item 🧪

# Escreva uma função usarItem(mochila, nomeItem) que recebe a mochila (lista de listas) e o nome de um item.
# Ela deve procurar o item e diminuir 1 da quantidade, e devolver (return) True se conseguiu usar, ou False se o item não existe ou a quantidade já é 0.

# Fora da função, teste assim:

# python
# mochila = [["pocao", 1], ["flecha", 20], ["tocha", 1]]
# Use "pocao" (deve dar True).
# Use "pocao" de novo (deve dar False, pois zerou).
# Use "espada" (deve dar False, não existe).

# Mostre, a cada teste, Usou pocao: True (com o nome e o resultado).

# Lembretes do seu histórico: return True dentro do loop é válido (achou e usou), mas o return False do “não achei” fica fora do for.
# Atenção: se achou a poção mas a quantidade é 0, também é False.

def usarItem(mochila, nomeItem):
    for item in mochila:
        if item[0] == nomeItem and item[1] > 0:
            item[1] -= 1
            return True
    return False

mochila = [["pocao", 1], ["flecha", 20], ["tocha", 1]]

resultado = usarItem(mochila, "pocao")
print(f"Usou pocao: {resultado}")

resultado = usarItem(mochila, "pocao")
print(f"Usou pocao: {resultado}")

resultado = usarItem(mochila, "espada")
print(f"Usou espada: {resultado}")