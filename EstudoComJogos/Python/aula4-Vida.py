# Vida do herói ❤️

# O herói começa com vida = 100. Ele enfrenta três monstros em sequência, e cada um tira uma quantidade de vida:

# python
# danos = [30, 25, 40]

# Percorra a lista danos com for e, a cada monstro, subtraia o dano da vida e mostre:

# Vida restante: 70
# Vida restante: 45
# Vida restante: 5

# Atenção: aqui a vida muda a cada volta. Cuidado para usar =/-= para atribuir, e não ==.

vida = 100
danos = [30, 25, 40]

for ataque in danos:
    vida -= ataque
    print(f"Vida restante: {vida}")

# Chave com função 🗝️

# Refaça o exercício 6, mas agora dentro de uma função temChave(mochila) que recebe a mochila como parâmetro e devolve (return) True se a chave estiver nela,
# ou False se não estiver. Fora da função, use o resultado para mostrar "Porta aberta!" ou "Porta trancada!".

# Teste com as duas mochilas:

# python
# mochilaA = ["machado", "escudo", "mapa", "tocha"]
# mochilaB = ["machado", "chave", "mapa"]

# Lembrete do seu ponto de atenção: return fica fora de qualquer loop, e aqui nem vai precisar de loop.

def temChave(mochila):
    for item in mochila:
        if item == "chave":
            return True
    return False

mochilaA = ["machado", "escudo", "mapa", "tocha"]
mochilaB = ["machado", "chave", "mapa"]

resultadoA = temChave(mochilaA)
if resultadoA == True:
    print("Porta aberta!")
else:
    print("Porta trancada!")

resultadoB = temChave(mochilaB)
if resultadoB == True:
    print("Porta aberta!")
else:
    print("Porta trancada!")