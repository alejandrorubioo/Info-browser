from flask import Blueprint, render_template

# Blueprint for /pepe route
logs_bp = Blueprint('logs', __name__)

@logs_bp.route('/pepe')
def ver_logs():
    try:
        with open("log_usuarios.json", "r") as f:
            contenido = f.readlines()
        return render_template("pepe.html", lineas=contenido)
    except:
        return "Log file not found"
