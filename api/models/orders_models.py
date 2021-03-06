from datetime import datetime
from enum import Enum

from ..utils import db


class Sizes(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer(), primary_key=True)
    size = db.Column(db.Enum(Sizes), default=Sizes.MEDIUM)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    user = db.Column(db.Integer(), db.ForeignKey("users.id"))

    def __repr__(self):
        return f"<Order {self.id}>"
