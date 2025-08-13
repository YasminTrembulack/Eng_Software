from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates", static_folder="static")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Estrtura de tabelas no DB
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), unique=True, nullable=False)


@app.route("/", methods=['GET'])
def index():
    return redirect('/task')

# CRUD - READ
@app.route("/task", methods=['GET'])
def list_tasks():
    tasks = Tarefa.query.all()
    return render_template("index.html", tasks_list=tasks)

# CRUD - CREATE
@app.route("/create/task", methods=['POST'])
def create_task():
    description = request.form['description']
    exists = Tarefa.query.filter_by(descricao=description).first()
    if exists:
        return 'Tarefa já cadastrada!', 400
    
    new_task = Tarefa(descricao=description)
    
    db.session.add(new_task)
    db.session.commit()

    return redirect('/task')
    
# CRUD - DELETE
@app.route("/delete/task/<int:task_id>", methods=['POST'])
def delete_task(task_id):
    task = Tarefa.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    
    return redirect('/task')

# CRUD - UPDATE
@app.route("/update/task/<int:task_id>", methods=['POST'])
def update_task(task_id):
    task = Tarefa.query.get(task_id)
    if task:
        task.descricao = request.form['description']
        db.session.commit()
    
    return redirect('/task')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
