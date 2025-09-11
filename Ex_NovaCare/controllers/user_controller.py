from flask import render_template, request, redirect, url_for

from models.appointment import User


def configure_routes(app):
    
    @app.route("/", methods=['GET'])
    def index():
        users = User.get_users()
        return render_template("index.html", users_list=users)
    
    @app.route('/contact')
    def contact():
        return render_template('contact.html')
    
    @app.route('/users/new', methods=['POST'])
    def create_user():
        User.create_user(
            name=request.form['name'],
            email=request.form['email'],
            birthday=request.form['birthday'],
            password=request.form['password']
        )
        return redirect(url_for('index'))
