from __future__ import absolute_import
import os

from flask import Flask, g
from osconf import config_from_environment


class AppSetup(object):

    def __init__(self):
        from backend.pool import Pool
        from .api import GisceStg
        self.api = GisceStg(prefix='/api')
        self.pool = Pool()

    def create_app(self, **config):
        """
        Create a gisce_stg app
        :param config:
        :return: gisce_stg app
        """
        app = Flask(__name__, static_folder=None)

        if 'SQLITE_DB' in os.environ:
            app.config['SQLITE_DB'] = os.environ['SQLITE_DB']

        app.config.update(config)

        self.configure_api(app)
        STGStandAlone.configure_stg(app)
        self.configure_backend(app)

        return app

    def configure_api(self, app):
        """
        Configure different API endpoints
        :param app: Flask application
        :return:
        """
        from .api import resources
        from .api.rtu import rtu_resources
        all_resources = resources + rtu_resources
        for resource in all_resources:
            self.api.add_resource(*resource)

        self.api.init_app(app)

    @staticmethod
    def configure_counter(app):
        """
        Configure SqliteCounter counter
        :param app:
        :return:
        """
        from .SqliteCounter import SqliteCounter
        app.counter = SqliteCounter(app.config['SQLITE_DB'])
        return app

    def setup_backend_conn(self):
        try:
            client = self.pool.connect(**config_from_environment('PEEK'))
            g.backend_cnx = client
        except Exception:
            pass

    def configure_backend(self, app):
        app.before_request(self.setup_backend_conn)


class STGStandAlone(object):

    @staticmethod
    def create_app(**config):
        app = Flask(__name__, static_folder=None)
        app.config.update(config)

        STGStandAlone.configure_stg(app)
        return app

    @staticmethod
    def configure_stg(app):
        from .stg import Stg, resources

        api = Stg(prefix='/stg')
        for resource in resources:
            api.add_resource(*resource)
        api.init_app(app, add_specs=False)
