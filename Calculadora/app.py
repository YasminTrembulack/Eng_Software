from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def calculadora():
    resultado = None

    if request.method == 'POST':
        num_01 = float(request.form['num_01'])
        num_02 = float(request.form['num_02'])
        op = request.form['op']
        
        match op:
            case 'soma':
                resultado = round(num_01 + num_02, 2)
            case 'subtracao':
                resultado = round(num_01 - num_02, 2)
            case 'multiplicacao':
                resultado = round(num_01 * num_02, 2)
            case 'divisao':
                if num_02 != 0:
                    resultado = round(num_01 / num_02, 2)
                else:
                    resultado = "Erro: divisão por zero"
            case _:
                resultado = "Operação inválida"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
