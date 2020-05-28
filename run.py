"""."""

import os

from app import create_app


config_name = os.getenv('APP_SETTINGS')  # config_name=developments
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
