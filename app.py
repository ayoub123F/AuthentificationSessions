from flask import Flask
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Configuration de la clé secrète pour les sessions
app.config['SECRET_KEY'] = 'your_secret_key'

# Configuration des blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)

# Configuration de la journalisation
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Configuration de la route pour la page d'accueil
@app.route('/')
def home():
    return 'Bienvenue sur la page d\'accueil !'

if __name__ == '__main__':
    app.run()

