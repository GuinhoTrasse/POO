console.log ("Papacu");

let nome = "Max Steel";
const sobrenome = "Steel";

console.log(nome, sobrenome);

function somar(a,b){
    return a+b
}

console.log(`${somar(1,2)} Dedos enfiados na bunda`);

class Pessoa{
    nome;
    sobrenome;
    cpf;
    id;

    constructor(nome, sobrenome, cpf, id)
    {
        this.nome = nome
        this.sobrenome = sobrenome
        this.cpf = cpf
        this.id = id
    }

    apresentar()
    {
        console.log(`Oi filho da puta, meu nome é ${this.nome} ${this.sobrenome}, eu te odeio, mas me odeio também, meu cpf é ${this.cpf}, use ele para acabar com a minha vida imediatamente`)
    }
}

cliente1 = new Pessoa();
cliente1.nome = "Bunda";
cliente1.sobrenome = "Fresca";
cliente1.cpf = "69";
cliente1.id = "69";

cliente2 = new Pessoa();
cliente2.nome = "Penis";
cliente2.sobrenome = "Passado";
cliente2.cpf = "96";

cliente3 = new Pessoa("Pintão", "Grandão", "67", "1")

cliente4 = new Pessoa("Palha", "Xota", "6969", "2")

cliente5 = new Pessoa("Dani", "Ficada", "20+20+20+7", "3")

cliente6 = new Pessoa("Cachorro", "Chupetão", "", "4")



cliente1.apresentar()
cliente2.apresentar()
cliente3.apresentar()
cliente4.apresentar()
cliente5.apresentar()
cliente6.apresentar()