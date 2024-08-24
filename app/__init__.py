from flask import Flask
from app.routes import init_routes

def create_app():
    app = Flask(__name__)
    

    app.config['SECRET_KEY'] = 'your_secret_key'

    init_routes(app)

    return app
