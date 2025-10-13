// importação do express
const express = require("express");

// instancia express
const app = express();


// O metodo GET é utilizado quando um cliente (navegador) quer obter dados de um servidor.

// O 1º argumento do metodo GET define qual caminho a logica implementada vai atender

// req - É um objeto que contem todas as infos sobre a requisição que chegou ao cliente (navegador)

// res - É um objeto que representa a resposta que o servidor vai enviar de volta para o cliente

// res.send() - Instrui o servidor a enviar uma resposta

app.get("/", function(req, res){
    res.send("<h1>Meu primeiro aplicativo com express</h1>")
})

// app.listen diz à aplicação para escutar por requisição HTTP

app.listen(8081, function(){
    console.log("Servidor esta funcionando");
})