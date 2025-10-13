const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));

// ___________________ BANCO DE DADOS 'Simulado' ___________________

const usuarios = [
  { id: 1, nome: "Yasmin", email: "yasmin@mail.com" },
  { id: 2, nome: "Eduardo", email: "eduardo@mail.com" },
  { id: 3, nome: "Maria", email: "maria@mail.com" },
];

// _____________________________ ROTAS _____________________________

app.get("/", (req, res) => {
  res.render("index", { usuarios });
});

//____________________________ SERVIDOR ___________________________

app.listen(port, () => {
    const url = `http://localhost:${port}`;
    console.log(`Servidor rodando em http://localhost:${port}`);

//     (async () => { ...})(): esta função async é iniciada. O javascript não espera ela terminar. ela apenas da o play e continua seu trabalho que no caso é 
//     app.listen, é manter o servidor no arch, pronto para receber requisições http(como app.get)

// O servidor ja esta funcionando e pronto para receber visitas Antes mesmo do navegador abrir
// O await pausa a execução SOMENTE DENTRO daquela função async especifica

    (async () => {
        try {
        
        // O await aqui diz: "Pare a excução desta função async"
        // ate que o import('open') seja finalizado/carregado
        // const open = require('open') é diferente de import ('open')
        //import('open') é chamada de importação dinamica
            const openModule = await import('open');

        // O await aqui diz: "Pare a execução desta função ASYNC NOVAMENTE"
        // Ate que a função de abrir o navegador termine".

            await openModule.default(url);
        } catch (error) {
            console.error('Error ao tentar abrir o navegador:', error);
        }
    })();
})
