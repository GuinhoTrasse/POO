# Contando as poções 🧪

# Você foi até a loja da vila e a mochila ficou assim:

# python
# mochila = ["pocao", "espada", "pocao", "mapa", "pocao", "tocha"]

# Percorra a mochila com for e use um if para contar quantas poções você tem. No final, mostre:

# Você tem 3 pocoes

# (O número deve vir da contagem do programa, não escrito na mão.)

mochila = ["pocao", "espada", "pocao", "mapa", "pocao", "tocha"]
quantidadeDePocao = 0

for pocoes in mochila:
    if pocoes == "pocao":
        quantidadeDePocao += 1

print(f"Você tem {quantidadeDePocao} pocoes")

# Tem a chave? 🗝️

# Para abrir a porta da masmorra, o jogador precisa ter "chave" na mochila. Com a lista abaixo, faça um programa que use if/else e mostre "Porta aberta!" se a chave estiver na mochila,
# ou "Porta trancada!" se não estiver.

# python
# mochila = ["machado", "escudo", "mapa", "tocha"]

# Depois, teste de novo adicionando "chave" na lista, para ver a outra mensagem aparecer.

# Dica de busca: o operador in serve para perguntar se um valor está dentro de uma lista.

mochila = ["machado", "escudo", "mapa", "tocha"]

if "chave" in mochila:
    print("Porta aberta!")
else:
    print("Porta trancada!")

mochila.append("chave")

if "chave" in mochila:
    print("Porta aberta!")
else:
    print("Porta trancada!")