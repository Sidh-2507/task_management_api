from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()  # Initialize JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')


    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)  # Initialize JWT with the app

    # Register blueprints
    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app
