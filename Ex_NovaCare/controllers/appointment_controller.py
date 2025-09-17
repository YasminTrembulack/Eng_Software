from flask import render_template, request, redirect, url_for

from models.appointment import Appointment


def configure_routes(app):
    
    @app.route("/", methods=['GET'])
    def index():
        appointments = Appointment.get_appointments()
        return render_template("index.html", appointments_list=appointments)
    
    @app.route('/contact')
    def contact():
        return render_template('contact.html')
    
    @app.route('/appointments/new', methods=['POST'])
    def create_appointment():
        Appointment.create_appointment(
            patient=request.form['patient'],
            doctor=request.form['doctor'],
            specialty=request.form['specialty'],
            date=request.form['date']
        )
        return redirect(url_for('index'))
