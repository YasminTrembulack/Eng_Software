import secrets
from flask import Flask
from controllers import cinema_ingressos_controller

# Maria Eduarda Selhorst
# Yasmin Trembulack Agostinho

app = Flask(__name__, template_folder="./views/templates", static_folder="./views/static")
app.secret_key = secrets.token_hex(32)

cinema_ingressos_controller.configure_routes(app)


if __name__ == "__main__":
    app.run(debug=True)