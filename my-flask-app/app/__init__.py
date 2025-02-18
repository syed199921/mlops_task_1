from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'
    app.register_blueprint(main)
    return app

app = create_app()