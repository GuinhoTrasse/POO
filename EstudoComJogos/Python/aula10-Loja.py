# A loja da vila 🛒

# A loja vende itens, e cada item é uma tupla (nome, preco). A loja inteira é uma lista de tuplas:

# python
# loja = [("espada", 150), ("escudo", 90), ("pocao", 25), ("arco", 120)]

# Percorra a loja com for nome, preco in loja: (desempacotando a tupla direto no for) e mostre só os itens que custam menos de 100 moedas:

# escudo custa 90 moedas
# pocao custa 25 moedas

# Atenção: como o for já separa a tupla em duas variáveis, nome e preco guardam cada uma um valor (nem posição, nem a lista inteira).

loja = [("espada", 150), ("escudo", 90), ("pocao", 25), ("arco", 120)]

for nome, preco in loja:
    if preco < 100:
        print(f"{nome} custa {preco} moedas")


# O item mais caro 💎

# Escreva uma função itemMaisCaro(loja) que recebe a lista de tuplas do exercício 16 e devolve dois valores: o nome e o preço do item mais caro.

# Fora da função, desempacote o retorno em duas variáveis e mostre:

# O item mais caro é espada por 150 moedas

# Lembretes do seu histórico: comece o recorde com None, atualize as duas variáveis juntas, e o return fica fora do for.

def itemMaisCaro(loja):
    itemCaro = None
    nomeItemCaro = ""

    for nome, preco in loja:
        if itemCaro == None:
            itemCaro = preco
            nomeItemCaro = nome
        if preco > itemCaro:
            itemCaro = preco
            nomeItemCaro = nome

    return nomeItemCaro, itemCaro

loja = [("espada", 150), ("escudo", 90), ("pocao", 25), ("arco", 120)]

resultado = itemMaisCaro(loja)
nome, preco = resultado
print(f"O item mais caro é {nome} por {preco} moedas")
