import logging

from flask import request
from flask_restplus import Resource
from app.api.helpers.business import create_product, update_product, delete_product
from app.api.helpers.serializers import products, page_of_products
from app.api.restplus import api
from app.database.models import Products
from app.api.orders.parser import pagination_arguments

import simplejson

log = logging.getLogger(__name__)

ns = api.namespace('products/prod1', description='Operations related to prod1')


@ns.route('/')
class ProductCollection(Resource):

	# @api.expect(pagination_arguments)
	# @api.marshal_with(page_of_orders)
	@api.marshal_list_with(products)
	def get(self):
		"""
		Returns list of orders.
		* test with markdown
		"""
		# product = Products.query.filter_by(product='prod1').all()
		return Products.query.all()
		# args = pagination_arguments.parse_args(request)
		# page = args.get('page', 1)
		# per_page = args.get('per_page', 10)

		# order_query = Orders.query
		# order_page = order_query.paginate(page, per_page, error_out=False)

		# return order_page


	@api.response(201, 'Product successfully created.')
	@api.expect(products)
	def post(self):
		"""
		Creates a new product.
		"""

		create_product(request.json)
		# return None, 201
		return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Product not found.')
class ProductItem(Resource):

	@api.marshal_with(products)
	def get(self, id):
		"""
		Returns a product.
		"""
		return Products.query.filter(Products.id == id).one()


	@api.expect(products)
	@api.response(204, 'Product successfully updated.')
	def put(self, id):
		"""
		Updates a product.
		"""
		update_product(id, request.json)
		return None, 204


	@api.response(204, 'Product successfully deleted.')
	def delete(self, id):
		"""
		Deletes a product.
		"""
		delete_product(id)
		return None, 204