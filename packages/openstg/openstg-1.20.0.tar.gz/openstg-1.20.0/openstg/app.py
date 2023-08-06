from __future__ import absolute_import
from openstg.config import AppSetup

application = AppSetup().create_app()

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True, use_reloader=False)
