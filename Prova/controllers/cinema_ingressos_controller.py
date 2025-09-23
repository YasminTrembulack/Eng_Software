from flask import render_template, request, redirect, flash

from models.cinema_ingressos import Ingresso


def configure_routes(app):
    
    @app.route('/', methods=['GET'])
    def index():
        try:
            ingressos = Ingresso.get_ingressos()
            return render_template('index.html', dados=ingressos)
        except Exception:
            flash('Erro ao buscar ingressos.', 'error')
            return render_template('index.html', dados=[])


    @app.route('/add', methods=['GET', 'POST'])
    def add_ingressos():
        if request.method == 'POST':
            try:
                Ingresso.create_ingresso(
                    nome_filme=request.form['nome_filme'],
                    genero=request.form['genero'],
                    sessoes=request.form['sessoes'],
                    nome_cliente=request.form['nome_cliente'],
                    assento=request.form['assento'],
                    data_filme=request.form['data_filme']
                )
                flash('Ingresso cadastrado com sucesso!', 'success')
            except Exception:
                flash('Erro ao cadastrar ingresso.', 'error')
        return render_template('upsert.html')

    @app.route('/edit/<int:ingresso_id>', methods=['GET', 'POST'])
    def update_ingresso(ingresso_id):
        if request.method == 'POST':
            Ingresso.update_ingresso(
                id=ingresso_id,
                nome_filme=request.form['nome_filme'],
                genero=request.form['genero'],
                sessoes=request.form['sessoes'],
                nome_cliente=request.form['nome_cliente'],
                assento=request.form['assento'],
                data_filme=request.form['data_filme']
            )
               
            flash('Ingresso atualizado com sucesso!', 'success')
            return redirect('/')

        elif request.method == 'GET':
            ingresso = Ingresso.get_ingresso(id=ingresso_id)        
            return render_template('upsert.html', ticket=ingresso)

    @app.route('/delete/<int:ingresso_id>', methods=['GET'])
    def delete_ingresso(ingresso_id):
        try:
            Ingresso.excluir_ingresso(id=ingresso_id)
            flash('Ingresso deletado com sucesso!', 'success')
        except Exception:
            flash('Erro ao deletar ingresso.', 'error')   
        return redirect('/')
