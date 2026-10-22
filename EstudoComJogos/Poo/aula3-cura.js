// Poção de cura 🧪

// Crie o método curar(quantidade), que soma a quantidade à vida. Mas a vida nunca pode passar de 100: se passar, ela fica exatamente em 100 (use if dentro do método).
// Teste com a Fernanda, que está com 30 de vida: cure 50 e mostre a vida, depois cure 50 de novo e mostre a vida.

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

    curar(quantidade) {
        this.vida = this.vida + quantidade
        if (this.vida > 100){
            this.vida = 100
        }
    }

    calcularPoder() {
        return this.nivel * 10 + this.vida
    }
}

const fernanda = new Personagem('Fernanda', 'Guerreiro', 50)

fernanda.curar(50)
console.log(fernanda.vida)
fernanda.curar(50)
console.log(fernanda.vida)

// Poder de combate 💪

// Crie o método calcularPoder(), que retorna o nível multiplicado por 10, somado à vida.

// Teste: crie a Fernanda (Guerreiro) com vida 50, faça ela subir de nível uma vez e mostre o poder dela com console.log.

// Antes de rodar, calcule no papel o resultado esperado e depois confira com o terminal. Lembre que um método que retorna usa return, e quem chama mostra com console.log(...).

fernanda.subirNivel()
console.log(fernanda.calcularPoder())