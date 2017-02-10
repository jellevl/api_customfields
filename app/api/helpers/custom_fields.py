import re 
from flask import abort
from flask_restplus import fields
from flask_restplus.fields import Raw, String, Integer
import simplejson as sjson

URL_REGEX = re.compile(r'(http|https|ftp)://\S+\.\S+')

class CustomField(Raw):
	"""
	Custom field base class with validation features
	"""
	# __schema__ = 'Raw'

	def __init__(self, *args, **kwargs):
		super(CustomField, self).__init__(**kwargs)
		# custom params
		self.positive = kwargs.get('positive', True)

	def format(self, value):
		"""
		format the text in database for output
		works only for GET requests
		"""
		if not self.validate(value):
			print 'Validation of field with value \"%s\" (%s) failed' %(
				value, str(self.__class__.name))
		# raise MarschallingError
		# Disabled for development purposes as the server chareshes when 
		# exception is raised. can be enabled when the project is mature
		if self.__schema_type__ =='string':
			return unicode(value)
		else:
			return value

	def validate_empty(self):
		"""
		Return when value is empty or null
		"""
		if self.required:
			return False
		else:
			return True

	def validate(self, value):
		"""
		Validate the value. Return True if valid.
		"""
		pass


class String(CustomField):
	"""
	Custom String field
	"""
	def validate(self, value):
		if not value:
			return self.validate_empty()
		if value.__class__.name__ in ['unicode', 'str']:
			return True
		else:
			return False

class Integer(CustomField):
	"""
	Custom Integer field
	"""
	__schema_type__ = 'integer'
	__schema__format__ = 'int'
	__schema__example__ = 0

	def validate(self, value):
		if value is None:
			return self.validate_empty()
		if type(value) != int:
			return False
		else:
			return True

class Float(CustomField):
	"""
	Custom Float field
	"""
	__schema_type__ = 'number'
	__schema__format__ = 'float'
	__schema__example__ = 0.0

	def validate(self, value):
		if value is None:
			return self.validate_empty()
		try:
			float(value)
			return True
		except Exception:
			return False



class Url(CustomField):
	"""
	Custom Url field
	"""
	__schema__format__ ='url'
	__schema_type__ = 'string'
	__schema__example__ = 'http://website.com/api'

	def validate(self, value):
		if value is None:
			return self.validate_empty()
		if not URL_REGEX.match(value):
			return False
		else:
			return True

class DateTime(CustomField):
	"""
	Custom DateTime field
	"""
	__schema__format__ = 'date-time'
	__schema_type__ = 'string'
	__schema__example__ = '2017-02-09 12:16:00'
	dt_format = '%Y-%m-%d %H:%M:%S'

	def to_sr(self, value):
		if value is None:
			return None
		else:
			return unicode(value.strftime(self.dt_format))

	def from_str(self, value):
		if value is None:
			return None
		else:
			return datetime.strptime(value, self.dt_format)

	def format(self, value):
		return self.to_str(value)

	def validate(self, value):
		if not value:
			return self.validate_empty()
		try:
			if value.__class__.__name__ in ['unicode', 'str']:
				self.from_str(value)
		except Exception:
				return False
		return True



"""
----------------------------------------------- More specific custom fields
"""
# class order_id(CustomField):
# 	"""
# 	order ID field
# 	"""
# 	__schema_type__ = 'integer'
# 	__schema__format__ = 'order_id'
# 	__schema__example__ = '12345'

# 	def validate(self, value):
# 		if not value:
# 			return self.validate_empty()
# 		if not value.length == 5:
# 			return False
# 		return True


class OrderID(CustomField):
	"""
	Custom OrderID field
	"""

	___schema_type__ = 'integer'
	___schema_format__ = 'integer'
	___schema_example__ = 12345
	__schema_description__ = 'blaat'

	def validate(self, value):
		if value.length != 5:
			return False
		else:
			return True


class Json(Raw):
	"""
	Custom JSON field
	"""
	def __init__(self, default=None, attribute=None, title=None, description=None, required=None, readonly=None, example=None, mask=None, **kwargs):
		self.attribute = attribute
		self.default = default
		self.title = title
		self.description = description
		self.required = required
		self.readonly = readonly
		self.example = example or self.__schema_example__
		self.mask = mask


	def format(self, value):
		value = sjson.loads(value)
		return value

	def validate(sef, value):
		try:
			value = sjson.loads(value)
		except Exception:
			return False

		for i in value:
			print i


