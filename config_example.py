# Flask settings
FLASK_SERVER_NAME = 'localhost:8080'
FLASK_DEBUG = True  # Do not use debug mode in production



# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'mysql://x:x@127.0.0.1/x'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False


# API settings
API_VERSION = '1.0'
API_TITLE = 'Title'
API_DESCRIPTION = 'Description'
API_SPEC_URL = '/api/swagger'