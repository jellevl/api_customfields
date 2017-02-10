from app.database import db
from app.database.models import Products
from datetime import datetime
import simplejson

def create_product(data):
	order_id = data.get('order_id')
	product_group = data.get('product_group')
	product = data.get('product')
	args = data.get('args')
	args = simplejson.dumps(args)
	request_origin = data.get('request_origin')
	request_callback = data.get('request_callback')
	product = Products(order_id, product_group, product, str(args), request_origin, request_callback)
	db.session.add(product)
	try:
		db.session.commit()
	except Exception, e:
		print str(e)


def update_product(id, data):
	product = Products.query.filter(Products.id == id).one()
	product.product_group = data.get('product_group')
	product.product = data.get('product')
	product.args = simplejson.dumps(data.get('args'))
	product.request_origin = data.get('request_origin')
	product.request_callback = data.get('request_callback')
	product.product = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	db.session.add(order)
	try:
		db.session.commit()
	except Exception, e:
		print str(e)


def delete_product(id):
	product = Products.query.filter(Products.id == id).one()
	db.session.delete(product)
	try:
		db.session.commit()
	except Exception, e:
		print str(e)
