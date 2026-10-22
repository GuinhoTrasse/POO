// Mochila de aventureiro 🎒

// Crie duas classes:

// Item, com nome e peso.
// Mochila, com uma lista itens que nasce vazia, o método guardar(item) e o método mostrarItens(), que mostra o nome de cada item usando for.

// Teste: crie 3 itens (Poção de peso 2, Espada de peso 8, Escudo de peso 10), guarde os três e chame mostrarItens().

class Item{
    constructor(nomeRecebido, pesoRecebido){
        this.nome = nomeRecebido
        this.peso = pesoRecebido
    }
}

class Mochila{
    constructor() {
        this.itens = []
    }

    guardar(item) {
        this.itens.push(item)
    }

    mostrarItens() {
        for (let i = 0; i < this.itens.length; i++) {
            console.log(this.itens[i].nome)
        }
    }

    pesoTotal() {
        let pesoAcumulado = 0
        for (let i = 0; i < this.itens.length; i++){
            pesoAcumulado += this.itens[i].peso
        }
        return pesoAcumulado
    }
}

const pocao = new Item('Poção', 2)
const espada = new Item('Espada', 8)
const escudo = new Item('Escudo', 10)
const mochila = new Mochila()
mochila.guardar(pocao)
mochila.guardar(espada)
mochila.guardar(escudo)

mochila.mostrarItens()

// Tá pesado! ⚖️

// Na classe Mochila, crie o método pesoTotal(), que retorna a soma dos pesos de todos os itens.

// Teste com os mesmos 3 itens e mostre o resultado com console.log. Calcule no papel o valor esperado antes de rodar.

// Cuidado com o seu erro frequente: return dentro do loop. Pense em onde o return deve ficar para a soma terminar antes de ser devolvida.
// E lembre de criar uma variável para ir acumulando a soma antes do for.

console.log(mochila.pesoTotal())