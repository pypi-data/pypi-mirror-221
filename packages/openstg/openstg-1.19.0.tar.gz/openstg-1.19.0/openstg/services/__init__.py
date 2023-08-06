from gisce import connect
from osconf import config_from_environment

class GISCEService:

    def __init__(self):
        uri_values = config_from_environment('ERP', ['db', 'user', 'password', 'uri'])

        self.c = connect(
            uri_values.get('uri'),
            uri_values.get('db'),
            user=uri_values.get('user'),
            password=uri_values.get('password')
        )

    def get_obj(self, obj):
        return self.c.model(obj)
