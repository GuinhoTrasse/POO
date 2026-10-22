class Candidato {
  constructor(numero, nome, partido) {
    this.numero = numero;
    this.nome = nome;
    this.partido = partido;
    this.votos = 0;
  }


  receberVoto() {
    this.votos++;
  }
}


class Urna {
  constructor() {
    this.candidatos = new Map();
    this.votosBrancos = 0;
    this.votosNulos = 0;
  }


  cadastrarCandidato(candidato) {
    this.candidatos.set(candidato.numero, candidato);
  }


  votar(numero) {
    if (numero === 0) {
      this.votosBrancos++;
      console.log("Voto em BRANCO registrado!");
    } else if (this.candidatos.has(numero)) {
      const candidato = this.candidatos.get(numero);
      candidato.receberVoto();
      console.log(`Voto confirmado para ${candidato.nome}!`);
    } else {
      this.votosNulos++;
      console.log("Voto NULO registrado!");
    }
  }


  exibirResultado() {
    console.log("\n==============================");
    console.log("     RESULTADO DA ELEIÇÃO     ");
    console.log("==============================");


    let totalVotos = this.votosBrancos + this.votosNulos;


    for (const candidato of this.candidatos.values()) {
      totalVotos += candidato.votos;
      console.log(`${candidato.nome} (${candidato.partido}): ${candidato.votos} voto(s)`);
    }


    console.log(`Votos em Branco: ${this.votosBrancos}`);
    console.log(`Votos Nulos: ${this.votosNulos}`);
  }
}


// --- EXECUÇÃO DA ELEIÇÃO 2026 ---


const urna = new Urna();


// Cadastrando pré-candidatos e figuras cotadas para a Eleição 2026
urna.cadastrarCandidato(new Candidato(13, "Lula", "PT"));
urna.cadastrarCandidato(new Candidato(10, "Tarcísio de Freitas", "Republicanos"));
urna.cadastrarCandidato(new Candidato(22, "Romeu Zema", "NOVO"));
urna.cadastrarCandidato(new Candidato(55, "Ronaldo Caiado", "PSD"));
urna.cadastrarCandidato(new Candidato(12, "Ciro Gomes", "PDT"));


console.log("=== INÍCIO DA VOTAÇÃO ==");


// Simulando sequência de votos na urna
const sequenciaDeVotos = [
  13, 10, 13, 22, 10, 13, 55, 0, 12, 13,
  10, 10, 13, 99, 10, 22, 13, 13, 0, 10
];


sequenciaDeVotos.forEach((numero) => urna.votar(numero));


// Exibição da apuração final
urna.exibirResultado();