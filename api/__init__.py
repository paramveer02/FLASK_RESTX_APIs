from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api

from .auth.views import auth_ns
from .config.config import config_dict
from .models.orders_models import Order
from .models.users_models import User
from .orders.views import orders_ns
from .utils import db


def create_app(config=config_dict["dev"]):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)

    api = Api(app)

    migrate = Migrate(app, db)

    api.add_namespace(orders_ns)
    api.add_namespace(auth_ns)

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db": db,
            "User": User,
            "Order": Order,
        }

    return app
