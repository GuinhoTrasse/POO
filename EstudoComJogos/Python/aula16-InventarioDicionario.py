# Inventário como dicionário 🎒

# O inventário agora é um dicionário {item: quantidade}:

# python
# inventario = {"pocao": 3, "flecha": 20, "tocha": 1}

# Escreva uma função usarItem(inventario, nomeItem) que devolve True se o item existe e tem quantidade maior que 0 (diminuindo 1 da quantidade), ou False caso contrário.
# Teste fora da função com "pocao", depois "espada", mostrando Usou pocao: True e Usou espada: False.

# Compare com o usarItem da lista de listas: aqui não precisa de for. O in e o acesso pela chave resolvem. O return False fica no fim da função.

def usarItem(inventario, nomeItem):
    if nomeItem in inventario and inventario[nomeItem] > 0:
        inventario[nomeItem] -= 1
        return True
    return False

inventario = {"pocao": 3, "flecha": 20, "tocha": 1}

resultado = usarItem(inventario, "pocao")
print(f"Usou pocao: {resultado}")

resultado = usarItem(inventario, "espada")
print(f"Usou espada: {resultado}")

# Ranking com lista de dicionários 🏆

# Cada jogador é um dicionário, e o ranking é uma lista de dicionários:

# python
# jogadores = [
#     {"nome": "Ana", "pontos": 1200},
#     {"nome": "Bruno", "pontos": 3400},
#     {"nome": "Carla", "pontos": 2800}
# ]

# Escreva uma função campeao(jogadores) que devolve o nome e os pontos do jogador com mais pontos (recorde começando com None). Fora da função, desempacote e mostre:

# O campeão é Bruno com 3400 pontos

# Atenção: no for jogador in jogadores:, jogador é o dicionário inteiro. O nome é jogador["nome"] e os pontos são jogador["pontos"]. O return fica fora do for.

jogadores = [
    {"nome": "Ana", "pontos": 1200},
    {"nome": "Bruno", "pontos": 3400},
    {"nome": "Carla", "pontos": 2800}
]

def campeao(jogadores):
    recorde = None
    melhorJogador = None
    for jogador in jogadores:
        if recorde == None:
            recorde = jogador["pontos"]
            melhorJogador = jogador["nome"]
        if jogador["pontos"] > recorde:
            recorde = jogador["pontos"]
            melhorJogador = jogador["nome"]
    return melhorJogador, recorde

melhorJogador, recorde = campeao(jogadores)
print(f"O campeão é {melhorJogador} com {recorde} pontos")