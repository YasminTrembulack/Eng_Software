import os
from flask import Flask, render_template
from controllers import user_controller


app = Flask(__name__, template_folder="./views/templates", static_folder="./views/static")
app.secret_key = os.urandom(32)



user_controller.configure_routes(app)


if __name__ == "__main__":
    app.run(debug=True)