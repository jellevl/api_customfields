#!env/bin/python
import logging.config

from flask import Flask, Blueprint, redirect
import config
# from rest_api_demo.api.blog.endpoints.posts import ns as blog_posts_namespace
# from rest_api_demo.api.blog.endpoints.categories import ns as blog_categories_namespace
# from app.api.orders.endpoints.ip_vpn_voice import ns as ip_vpn_voice_namespace
from app.api.products.prod1.endpoint import ns as prod1
from app.api.restplus import api
from app.database import db

app = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = config.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_ECHO'] = config.SQLALCHEMY_ECHO
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = config.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = config.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = config.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = config.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    # api.add_namespace(ip_vpn_voice_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)
    @app.route('/')
    def redirecttoapi():
        return redirect('/api', 302)

def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=config.FLASK_DEBUG)

if __name__ == "__main__":
    main()
