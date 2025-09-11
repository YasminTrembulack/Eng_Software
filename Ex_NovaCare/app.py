from collections import defaultdict
import os
import mysql.connector

from flask import Flask, render_template, request, redirect, flash

from config import db_config

app = Flask(__name__, template_folder="./views/templates", static_folder="./views/static")
app.secret_key = os.urandom(24)


# CRUD - READ
@app.route("/", methods=['GET'])
def list_appointments():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM nc_appointments")
    appointments_list = cursor.fetchall()
    
    appointments_by_date = defaultdict(list)
    for a in appointments_list:
        date_str = a['data_consulta'].date()
        appointments_by_date[date_str].append(a)

    cursor.close()
    conn.close()
    
    return render_template("index.html", appointments=appointments_by_date)


# CRUD - CREATE
@app.route("/create/appointment", methods=['GET','POST'])
def create_appointment():
    ...
#     if request.method == 'GET':
#         return render_template("upsert.html")

#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor(dictionary=True)
    
#     nome = request.form['description']
#     aniversario = request.form['birthday']
#     email = request.form['email']
#     senha = request.form['password']
    
#     cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#     existing_user = cursor.fetchone()

#     if existing_user:
#         cursor.close()
#         conn.close()
#         flash("Usuário já cadastrado com esse email!", 'error')
#         return render_template("upsert.html")

#     insert_query = """
#         INSERT INTO users (nome, aniversario, email, senha) 
#         VALUES (%s, %s, %s, %s)
#     """
#     cursor.execute(insert_query, (nome, aniversario, email, senha))
#     conn.commit()

#     cursor.close()
#     conn.close()
    
#     flash('Usuário cadastrado com sucesso!', 'success')

#     return redirect('/')

# CRUD - UPDATE
@app.route("/update/appointment/<int:appointment_id>", methods=['POST', 'GET'])
def update_appointment(appointment_id):
    ...
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor(dictionary=True)
    
#     if request.method == "POST":
#         nome = request.form['description']
#         aniversario = request.form['birthday']
#         email = request.form['email']
        
#         cursor.execute("""
#             UPDATE users 
#             SET nome = %s, email = %s, aniversario = %s
#             WHERE id = %s
#         """, (nome, email, aniversario, user_id))

#         conn.commit()

#         cursor.close()
#         conn.close()
#         return redirect('/')
    
#     else:
#         cursor.execute("SELECT id, nome, email, aniversario FROM users WHERE id = %s", (user_id,))
#         user = cursor.fetchone()
        
#         cursor.close()
#         conn.close()
#         return render_template("upsert.html", user=user)

    
# CRUD - DELETE
@app.route("/delete/appointment/<int:appointment_id>", methods=['GET'])
def delete_appointment(appointment_id):
    ...
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("""
#         DELETE FROM users
#         WHERE id = %s
#     """, (user_id,))
    
#     conn.commit()

#     cursor.close()
#     conn.close()
    
#     return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
