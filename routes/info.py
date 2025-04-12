from flask import Blueprint, request
from utils.helpers import guardar_log

# Blueprint for /info route
info_bp = Blueprint('info', __name__)

@info_bp.route('/info', methods=['POST'])
def recibir_info():
    # Receive JSON data from client-side JavaScript
    data = request.get_json()
    guardar_log(data, request)  # Save it to log
    return '', 204
