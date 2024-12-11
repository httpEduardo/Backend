from flask import Flask
from database import initialize_database
from config import DevelopmentConfig  # Importa as configurações de desenvolvimento

def create_app():
    app = Flask(__name__)  # Inicializa a aplicação Flask
    app.config.from_object(DevelopmentConfig)  # Aplica as configurações de desenvolvimento

    initialize_database()

    with app.app_context():
        from .routes import register_routes
        register_routes(app)

    return app
