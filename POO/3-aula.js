class BancoCentral{
    static transferirValor(emitente, destino, valor, senha)
    {
        if(emitente.sacar(valor, senha))
        destino.depositoViaBC(valor);
    }
}


class Pessoa{
    #cpf
    #nome
    #dataNasc
    #endereco


    get nome()
    {
        return this.#nome;
    }


    constructor(cpf, nome, dataNasc)
    {
        this.#cpf = cpf
        this.#nome = nome
        this.#dataNasc = dataNasc
    }


    criarConta()
    {
        return new Conta(this)
    }
}


class Conta{
    #senha = 'admin'
    #dono
    #saldo
    constructor(dono)
    {
        this.#saldo = 0;
        this.#dono = dono
    }


    //get sempre retorna algo
    get saldo()
    {
        if (this.#saldo <= 300)
            return this.#saldo
        else
            return 'Valor impede demonstração'
    }


    //set atualiza o valor
    set saldo(valor)
    {
        this.#saldo += valor;
    }


    sacar(valorSaque, senha)
    {
        if(valorSaque <= 0)
        {
            console.log('Não é possível sacar valor negativo')
            return false
        }
        if(!this.validarSenha(senha))
        {
            console.log('Senha incorreta')
            return false
        }
        if((this.#saldo - valorSaque) >= 0)
        {
            this.#saldo -= valorSaque
            return true
        }
        else
        {
            console.log('Saldo insuficiente')
            return false
        }
    }


    extrato(senha)
    {
        if(!this.validarSenha(senha))
        {
            console.log('Senha incorreta')
            return
        }
        console.log(`${this.#dono.nome}, Seu saldo é ${this.#saldo}`)
    }


    depositar(valor, senha)
    {
        if(!this.validarSenha(senha))
        {
            console.log('Senha incorreta')
            return
        }
        if(valor < 0)
        {
            console.log('O valor depositado não pode ser negativo')
            return;
        }
        if(valor > 5000)
        {
            console.log('Valor muito alto. Dirija-se ao caixa. Atendimento das 10:00h às 15:00h')
            return;
        }
        this.#saldo += valor
    }


    depositoViaBC(saldo)
    {
        this.#saldo += saldo
    }


    validarSenha(senha)
    {
        return senha === this.#senha
    }


    exibirDadosContas()
    {
        return this.#dono.nome
    }
}


    
    class Banco{
        #contas = [];


        addConta(conta)
        {
            this.#contas.push(conta)
        }


        exibirContasRegistradas()
        {
            console.log("Donos de conta deste banco:")
            this.#contas.forEach( conta => {
                console.log (conta.exibirDadosContas())
            })
        }


    }




Jose = new Pessoa('126365', 'José Silva', '10/10/1988')
Manoel = new Pessoa('123654', 'Manoel Costa', '10/10/2010')


santander = new Banco()


// Primeira maneira de criar uma conta
santander.addConta(Jose.criarConta())


// Segunda maneira de criar uma conta
contaManoel = Manoel.criarConta()
santander.addConta(contaManoel)


santander.exibirContasRegistradas()


// Fazer operação de transferência
//contaJose.depositar(50, 'admin')
//contaManoel.depositar(150, 'admin')
//contaJose.extrato('admin')
//contaManoel.extrato('admin')
//contaCopia.extrato('admin')


// BC = new BancoCentral()
//BancoCentral.transferirValor(contaJose, contaManoel, 500, 'admin')


//contaJose.extrato('admin')
//contaManoel.extrato('admin')
//contaCopia.extrato('admin')
//contaCopia2 = contaCopia


//contaCopia.depositar(1000, 'admin')
//console.log('----------------------------------------------------------------------------------')


//contaJose.extrato('admin')
//contaManoel.extrato('admin')
//contaCopia.extrato('admin')