from flask_restplus import fields
from app.api.restplus import api
from app.api.helpers import custom_fields as CustomField

products = api.model('products', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an order'),
    'order_id': fields.Integer(required=True, description='Product order ID', min_length=5, max_length=5),
    'product_group': fields.String(required=True, description='Product group', example='product_group'),
    'product': fields.String(required=True, description='Product name', example='prod1'),
    'args': CustomField.Json(required=True, description='Product arguments in JSON format', example={"foo":"bar"}),
    'request_origin': fields.String(required=True, description='Request Origin', example='127.0.0.1'),
    'request_callback': fields.Url(required=True, description='Request callback url', example='http://origin.com/callback_uri'),
    'created_at': fields.DateTime(readOnly=True, description='Product creation date'),
    'updated_at': fields.DateTime(readOnly=True, description='product last update date'),
})


pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_products = api.inherit('Page of products', pagination, {
    'items': fields.List(fields.Nested(products))
})