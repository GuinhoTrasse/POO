# O herói sobreviveu? 💀

# Escreva uma função somaDanos(listaDanos) que recebe uma lista de danos e devolve a soma total deles. Depois, fora da função, use o resultado para decidir:

# se o total for maior ou igual a 100, mostre "Game over!";
# senão, mostre "O herói sobreviveu!".

# Teste com:

# python
# danosFase1 = [30, 25, 40]
# danosFase2 = [50, 35, 20]

def somaDanos(listaDanos):
    total = 0
    for dano in listaDanos:
        total += dano
    return total

danosFase1 = [30, 25, 40]
danosFase2 = [50, 35, 20]

totalFase1 = somaDanos(danosFase1)
if totalFase1 >= 100:
    print("Game over!")
else:
    print("O herói sobreviveu!")

totalFase2 = somaDanos(danosFase2)
if totalFase2 >= 100:
    print("Game over!")
else:
    print("O herói sobreviveu!")

# Loot do monstro 💎

# Um monstro derrotado deixou cair estes itens, cada um com um valor em moedas:

# python
# loot = ["adaga", "gema", "pele", "anel"]
# valores = [15, 80, 5, 40]

# Use um for com range(len(loot)) para mostrar, em cada linha, o item e seu valor:

# adaga vale 15 moedas
# gema vale 80 moedas
# ...

# Atenção: com range, a variável do for guarda a posição, não o valor. Você vai precisar usá-la dentro dos colchetes das duas listas.

loot = ["adaga", "gema", "pele", "anel"]
valores = [15, 80, 5, 40]

for posicao in range(len(loot)):
    print(f"{loot[posicao]} vale {valores[posicao]} moedas")