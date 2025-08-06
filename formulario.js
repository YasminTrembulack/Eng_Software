class Contato {
    constructor() {
        this.nome = null;
        this.email = null;
        this.fone = null;
        this.mensagem = null;
        this.data_cadastro = null;
        this.tipo_contato = null;
    }

    Enviar(e) {
        e.preventDefault();
        this.removerErros();

        this.nome = document.getElementById('nome').value.trim();
        this.email = document.getElementById('email').value.trim();
        this.fone = document.getElementById('telefone').value.trim();
        this.mensagem = document.getElementById('mensagem').value.trim();
        this.data_cadastro = document.getElementById('data_cadastro').value.trim();
        this.tipo_contato = document.getElementById('tipo_contato').value.trim();

        const campos = [
            { id: 'nome', valor: this.nome, nome: 'Nome' },
            { id: 'email', valor: this.email, nome: 'Email' },
            { id: 'telefone', valor: this.fone, nome: 'Telefone' },
            { id: 'mensagem', valor: this.mensagem, nome: 'Mensagem' },
            { id: 'data_cadastro', valor: this.data_cadastro, nome: 'Data de cadastro' },
            { id: 'tipo_contato', valor: this.tipo_contato, nome: 'Tipo de contato' }
        ];

        let camposInvalidos = [];

        campos.forEach(campo => {
            if (campo.valor === '') {
                document.getElementById(campo.id).classList.add('erro');
                camposInvalidos.push(campo.nome);
            }
        });

        if (camposInvalidos.length > 0) {
            alert('Por favor, preencha os campos obrigatórios: ' + camposInvalidos.join(', '));
            return;
        }

        this.adicionarNaTabela();
        console.log("AAAAAAAAA")
        this.limparFormulario();
        alert('Dados cadastrados com sucesso!');
    }

    removerErros() {
        const inputs = document.querySelectorAll('input');
        inputs.forEach(input => input.classList.remove('erro'));
    }

    adicionarNaTabela() {
        const tabela = document.getElementById('grid');
        const novaLinha = tabela.insertRow(-1);

        novaLinha.innerHTML = `
            <td>${this.nome}</td>
            <td>${this.email}</td>
            <td>${this.telefone}</td>
            <td>${this.mensagem}</td>
            <td>${this.data_cadastro}</td>
            <td>${this.tipo_contato}</td>
        `;
    }

    limparFormulario() {
        document.querySelector('form').reset();
    }
}

const contato = new Contato();