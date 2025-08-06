from flask import Flask, render_template

# O name faz referencia ao proprio arquivo e garente que a aplicação vai rodar
app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def main():
    mensagem = "Oláaaa"
    return render_template("index.html", mensagem=mensagem)


@app.route("/brasileirao")
def brasileirao():
    mensagem = "Brasileirão 2025"
    brasileirao_2025 = [
        {"position": 1, "name": "Palmeiras", "city": "São Paulo", "points": 45},
        {"position": 2, "name": "Flamengo", "city": "Rio de Janeiro", "points": 44},
        {"position": 3, "name": "Atlético-MG", "city": "Belo Horizonte", "points": 41},
        {"position": 4, "name": "Grêmio", "city": "Porto Alegre", "points": 39},
        {"position": 5, "name": "São Paulo", "city": "São Paulo", "points": 38},
        {"position": 6, "name": "Botafogo", "city": "Rio de Janeiro", "points": 36},
        {
            "position": 7,
            "name": "Red Bull Bragantino",
            "city": "Bragança Paulista",
            "points": 35,
        },
        {"position": 8, "name": "Internacional", "city": "Porto Alegre", "points": 34},
        {"position": 9, "name": "Athletico-PR", "city": "Curitiba", "points": 32},
        {"position": 10, "name": "Fortaleza", "city": "Fortaleza", "points": 31},
        {"position": 11, "name": "Cuiabá", "city": "Cuiabá", "points": 29},
        {"position": 12, "name": "Bahia", "city": "Salvador", "points": 28},
        {"position": 13, "name": "Cruzeiro", "city": "Belo Horizonte", "points": 27},
        {"position": 14, "name": "Corinthians", "city": "São Paulo", "points": 26},
        {
            "position": 15,
            "name": "Vasco da Gama",
            "city": "Rio de Janeiro",
            "points": 24,
        },
        {"position": 16, "name": "Santos", "city": "Santos", "points": 23},
        {"position": 17, "name": "Atlético-GO", "city": "Goiânia", "points": 21},
        {"position": 18, "name": "Vitória", "city": "Salvador", "points": 19},
        {"position": 19, "name": "Juventude", "city": "Caxias do Sul", "points": 18},
        {"position": 20, "name": "Criciúma", "city": "Criciúma", "points": 16},
    ]
    return render_template("table.html", title=mensagem, list=brasileirao_2025)


@app.route("/teams")
def teams():
    mensagem = "Brasileirão 2025"
    team_names = [
        "Palmeiras",
        "Flamengo",
        "Atlético-MG",
        "Grêmio",
        "São Paulo",
        "Botafogo",
        "Red Bull Bragantino",
        "Internacional",
        "Athletico-PR",
        "Fortaleza",
        "Cuiabá",
        "Bahia",
        "Cruzeiro",
        "Corinthians",
        "Vasco da Gama",
        "Santos",
        "Atlético-GO",
        "Vitória",
        "Juventude",
        "Criciúma",
    ]
    return render_template("simple_table.html", title=mensagem, list=team_names)


if __name__ == "__main__":
    app.run(debug=True)
    # Modo debug: mostra os erros de forma detalhada e atualiza caso tenha uma mudança no código
