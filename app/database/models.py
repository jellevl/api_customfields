# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime
from app.database import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    product_group = db.Column(db.String(255))
    product = db.Column(db.String(255))
    args = db.Column(db.Text)
    request_origin = db.Column(db.String(255))
    request_callback = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    # aanvullen met overige velden.

    def __init__(self, order_id, product_group, product, args, request_origin, request_callback, created_at=None, updated_at=None):
        self.order_id = order_id
        self.product_group = product_group
        self.product = product
        self.args = args
        self.request_origin = request_origin
        self.request_callback = request_callback
        # self.created_at = created_at
        # self.updated_at = updated_at
        

        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if created_at is None:
            self.created_at = dt
        if updated_at is None:
            self.updated_at = dt

    def __repr__(self):
        return '<Product %r>' % self.order_id