// O herói nasce
// Crie Personagem com nome, classe e vida. Crie dois personagens diferentes e mostre o nome e a vida de cada um.

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

}

const miguel = new Personagem('Miguel', 'Druida', 30)
const fernanda = new Personagem('Fernanda', 'Guerreiro', 50)

console.log(miguel.nome)
console.log(miguel.vida)
console.log(fernanda.nome)
console.log(fernanda.vida)

// Use a sua classe Personagem e acrescente:

// Um atributo nivel que sempre começa em 1 (sem vir como parâmetro do constructor).
// Um método subirNivel() que soma 1 ao nível do personagem (dica: o += que você já conhece do Python funciona igual).

// Depois, em um dos personagens, mostre o nível, chame subirNivel() duas vezes e mostre o nível de novo.

console.log(`Nível do Miguel: ${miguel.nivel}`)
miguel.subirNivel()
miguel.subirNivel()
console.log(`Nível do Miguel: ${miguel.nivel}`)