from flask import render_template, request, redirect, flash

from models.task import Tarefa


def configure_routes(app):
    
    @app.route('/', methods=['GET'])
    def index():
        try:
            tarefas = Tarefa.get_tasks()
            print(tarefas)
            return render_template('index.html', dados=tarefas)
        except Exception:
            flash('Erro ao buscar tarefas.', 'error')
            return render_template('index.html', dados=[])


    @app.route('/add', methods=['GET', 'POST'])
    def add_task():
        if request.method == 'POST':
            try:
                Tarefa.create_task(
                    title=request.form['title'],
                    description=request.form['description'],
                    priority=request.form['priority']
                )
                flash('Tarefa cadastrado com sucesso!', 'success')
            except Exception:
                flash('Erro ao cadastrar tarefa.', 'error')
        return render_template('upsert.html')

    @app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
    def update_task(task_id):
        if request.method == 'POST':
            Tarefa.update_task(
                id=task_id,
                title=request.form['title'],
                description=request.form['description'],
                status=request.form['status'],
                priority=request.form['priority']            )
               
            flash('Tarefa atualizado com sucesso!', 'success')
            return redirect('/')

        elif request.method == 'GET':
            tarefa = Tarefa.get_task(id=task_id)        
            return render_template('upsert.html', task=tarefa)
            
    @app.route('/delete/<int:task_id>', methods=['GET'])
    def delete_task(task_id):
        try:
            Tarefa.excluir_task(id=task_id)
            flash('Tarefa deletada com sucesso!', 'success')
        except Exception:
            flash('Erro ao deletar tarefa.', 'error')   
        return redirect('/')