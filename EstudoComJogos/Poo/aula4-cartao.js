// Cartão do personagem 🪪

// Até agora, console.log(fernanda) mostra a estrutura do objeto, com aquelas chaves.
// Para um objeto mostrar um texto próprio quando é convertido em texto, a classe pode ter um método chamado toString() (o equivalente ao __str__ do Python).
// Ele retorna uma string, e o JS usa esse texto automaticamente dentro de uma template string.

// Exemplo com a Espada (só a forma):

// javascript
// class Espada {
//     constructor(nomeRecebido, danoRecebido) {
//         this.nome = nomeRecebido
//         this.dano = danoRecebido
//     }

//     toString() {
//         return `${this.nome} causa ${this.dano} de dano`
//     }
// }

// const espada1 = new Espada('Excalibur', 50)
// console.log(`${espada1}`)

// Saída: Excalibur causa 50 de dano

// Atenção: o console.log(espada1) sozinho não usa o toString(). O texto aparece quando o objeto está dentro de ${...} ou de uma soma de texto.

// Enunciado: na classe Personagem, crie o toString() para retornar um texto neste formato: Fernanda | Guerreiro | Nível 1 | Vida 50.
// Teste com a Fernanda (Guerreiro, vida 50) usando console.log(${fernanda}).

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

    toString() {
        return `${this.nome} | ${this.classe} | Nível ${this.nivel} | Vida ${this.vida}`
    }

    atacar(alvo) {
        alvo.receberDano(this.nivel * 5)
    }
}

const fernanda = new Personagem('Fernanda', 'Guerreiro', 50)
const miguel = new Personagem('Miguel', 'Druida', 30)
console.log(`${fernanda}`)
console.log(fernanda.toString())

// Ataque! ⚔️

// Na classe Personagem, crie o método atacar(alvo), em que o alvo é outro Personagem.
// O alvo deve receber de dano o nível do atacante vezes 5. Use o método receberDano do alvo para isso.

// Teste: o Miguel (Druida, vida 30) sobe uma vez de nível e ataca a Fernanda (Guerreiro, vida 50).
// Mostre a vida da Fernanda antes e depois do ataque. Calcule no papel o resultado antes de rodar.

miguel.subirNivel()
console.log(fernanda.vida)
miguel.atacar(fernanda, miguel)
console.log(fernanda.vida)