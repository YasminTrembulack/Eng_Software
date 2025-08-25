import os
from flask import Flask, render_template, request, redirect, flash, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="templates", static_folder="static")

UPLOAD_FOLDER = 'C:\\Users\\yastr\\Desktop\\Projects\\Faculdade\\Aula02\\diretorio'


@app.route("/", methods=['GET'])
def index():
    arquivos = []
    
    for nome_arquivo in os.listdir(UPLOAD_FOLDER):
        caminho = os.path.join(UPLOAD_FOLDER, nome_arquivo)
        if os.path.isfile(caminho):
            arquivos.append(nome_arquivo)
            
    return render_template('index.html', arquivos=arquivos)    


if __name__ == "__main__":
    app.run(debug=True)
