from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
import os

load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()
oauth = OAuth()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.secret_key = os.getenv('SECRET_KEY')

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    oauth.init_app(app)

    # Register Auth0
    oauth.register(
        "auth0",
        client_id=os.getenv("AUTH0_CLIENT_ID"),
        client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
        client_kwargs={"scope": "openid profile email"},
        server_metadata_url=f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/openid-configuration',
    )

    # Register blueprints
    from app.routes.customer import customer_bp
    from app.routes.order import order_bp
    from app.routes.auth import auth_bp
    app.register_blueprint(customer_bp, url_prefix='/api/customers')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    app.register_blueprint(auth_bp, url_prefix='/api/auth/login')

    return app
