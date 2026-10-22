# Item mais barato 🪙

# Escreva uma função itemMaisBarato(loja) com a mesma lista do exercício 16, que devolve dois valores: o nome e o preço do item mais barato. Fora da função, desempacote e mostre:

# O item mais barato é pocao por 25 moedas

# Dica de caminho: é o mesmo padrão do 17, só muda a direção da comparação. Atenção ao lugar do None: antes do for, e em itemBarato, não em preco.

def itemMaisBarato(loja):
    itemBarato = None
    nomeItemBarato = ""
    for item, preco in loja:
        if itemBarato == None:
            itemBarato = preco
            nomeItemBarato = item
        if itemBarato > preco:
            itemBarato = preco
            nomeItemBarato = item
    return itemBarato, nomeItemBarato

loja = [("espada", 150), ("escudo", 90), ("pocao", 25), ("arco", 120)]

resultado = itemMaisBarato(loja)
preco, nome = resultado
print(f"O item mais barato é {nome} por {preco} moedas")

# Gastando moedas 💰

# O herói tem moedas = 100 e quer comprar itens da loja, na ordem em que aparecem na lista:

# python
# loja = [("espada", 150), ("escudo", 90), ("pocao", 25), ("arco", 120)]

# Percorra a loja com for nome, preco in loja:. Para cada item:

# se o herói tem moedas suficientes (moedas >= preco), ele compra: subtraia o preço das moedas e mostre Comprou escudo, sobram 10 moedas;
# senão, mostre Sem moedas para espada.

# Saída esperada:

# Sem moedas para espada
# Comprou escudo, sobram 10 moedas
# Sem moedas para pocao
# Sem moedas para arco

# Atenção: as moedas mudam durante o loop, então use -= para atribuir (nada de ==). Repare que, depois de comprar o escudo, sobram 10 moedas, e por isso a poção de 25 já não dá.

loja = [("espada", 150), ("escudo", 90), ("pocao", 25), ("arco", 120)]

moedas = 100

for nome, preco in loja:
    if moedas - preco >= 0:
        moedas -= preco
        print(f"Comprou {nome}, sobram {moedas} moedas")
    else:
        print(f"Sem moedas para {nome}")