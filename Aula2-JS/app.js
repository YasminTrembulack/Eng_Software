const express = require("express");
const mysql = require("mysql2");
const path = require("path");

const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.static(path.join(__dirname, "public")));

// ___________________ BANCO DE DADOS  ___________________

const pool = mysql.createPool({
  connectionLimit: 10,
  host: "localhost",
  user: "root",
  password: "root",
  database: "backend_development",
});

console.log("Pooll de conexão com o MySQL criado com sucesso!");

// _____________________________ ROTAS _____________________________


app.get("/", (req, res) => {
    const sqlQuery = "SELECT * FROM products;";

    pool.query(sqlQuery, (error, result) => {
        if (error) {
            console.log("Erro ao buscar produtos:", error);
            return res.render("produtos", { produtos: [] });
        }
        res.render("produtos", { produtos: result || [] });
    });
});


app.get("/adicionar", (req, res) => {
    const { nome, preco, descricao } = req.body;

    pool.query(sqlQuery, [nome, preco, descricao], (error, result) => {
        if(error){
            const errorMessage = "Erro ao criar produto.";
            console.log(errorMessage, error);
            return res.status(500).send(errorMessage);
        }
        console.log("Produto criado com sucesso!");
        res.redirect("/");
    });
});


app.get("/editar/:id", (req, res) => {
    const { id } = req.params;

    const sqlQuery = "SELECT * FROM products WHERE id = ?;"
    pool.query(sqlQuery, (error, result) => {
        if(error){
            const errorMessage = "Erro ao buscar produto por ID. ";
            console.log(errorMessage, error);
            return res.status(500).send(errorMessage);
        }
        if (result === 0){
            return res.status(404).send("Produto não encontrado.");
        }
    });
    console.log("Produto criado com sucesso!")
    res.redirect("edit_produto", {produto: result[0]});
});

//____________________________ SERVIDOR ___________________________

app.listen(port, () => {
  const url = `http://localhost:${port}`;
  console.log(`Servidor rodando em http://localhost:${port}`);

  (async () => {
    try {
      const openModule = await import("open");
      await openModule.default(url);
    } catch (error) {
      console.error("Error ao tentar abrir o navegador:", error);
    }
  })();
});
