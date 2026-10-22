// Ai, doeu! 💥

// Na classe Personagem, crie o método receberDano(dano), que diminui a vida do personagem pelo valor recebido.
// Depois faça a Fernanda receber 20 de dano e mostre a vida dela antes e depois.

class Personagem{
    constructor(nomeRecebido, classeRecebida, vidaRecebida){
        this.nome = nomeRecebido
        this.classe = classeRecebida
        this.vida = vidaRecebida
        this.nivel = 1
    }

    subirNivel() {
        this.nivel += 1
    }

    receberDano(dano) {
        this.vida -= dano
    }

    estaVivo() {
        if (this.vida > 0){
            return true
        } else {
            return false
        }
    }
}

const fernanda = new Personagem('Fernanda', 'Guerreiro', 50)
const miguel = new Personagem('Miguel', 'Druida', 30)

console.log(`Vida da Fernanda antes: ${fernanda.vida}`)
fernanda.receberDano(20)
console.log(`Vida da Fernanda depois: ${fernanda.vida}`)

// Ainda tá vivo? 🧟

// Crie o método estaVivo(), que retorna true se a vida for maior que 0 e false caso contrário (use if/else normal).
// Depois faça o Miguel receber 40 de dano e mostre o resultado de miguel.estaVivo() com console.log.

// Dois lembretes:

// O Miguel nasce com vida 30, então depois de 40 de dano a vida dele fica negativa. Pense no que o método deve responder nesse caso.
// Método que retorna algo usa return, e quem chama mostra o resultado com console.log(...).

miguel.receberDano(40)
console.log(miguel.estaVivo())