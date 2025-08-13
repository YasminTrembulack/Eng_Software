import os
import mysql.connector
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.urandom(24)


db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'backend_development'
}


# CRUD - READ
@app.route("/", methods=['GET'])
def list_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("index.html", users_list=data)


# # CRUD - CREATE
@app.route("/create/user", methods=['GET','POST'])
def create_user():
    if request.method == 'GET':
        return render_template("create.html")

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    nome = request.form['description']
    aniversario = request.form['birthday']
    email = request.form['email']
    senha = request.form['password']
    
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.close()
        conn.close()
        return "Usuário já cadastrado com esse email!", 400

    insert_query = """
        INSERT INTO users (nome, aniversario, email, senha) 
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (nome, aniversario, email, senha))
    conn.commit()

    cursor.close()
    conn.close()
    
    flash('Usuário cadastrado com sucesso!')

    return redirect('/')
    
# # CRUD - DELETE
# @app.route("/delete/task/<int:task_id>", methods=['POST'])
# def delete_task(task_id):
#     task = Tarefa.query.get(task_id)
#     if task:
#         db.session.delete(task)
#         db.session.commit()
    
#     return redirect('/task')

# # CRUD - UPDATE
# @app.route("/update/task/<int:task_id>", methods=['POST'])
# def update_task(task_id):
#     task = Tarefa.query.get(task_id)
#     if task:
#         task.descricao = request.form['description']
#         db.session.commit()
    
#     return redirect('/task')


if __name__ == "__main__":
    app.run(debug=True)
