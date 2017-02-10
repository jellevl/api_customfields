class order_id(CustomField):
	"""
	orderid field
	"""
	__schema_type__ = 'integer'
	__schema_format__ = "int"
	__schema_example__ = "12345"

	def validate(self, value):
		if not value:
			return self.validate_empty()
		if type(value) != int:
			return False
		if value.lenght !== 5:
			return False
			
