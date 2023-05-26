# import os
from app import create_app

# settings_module = os.getenv("APP_SETTINGS_MODULE")
settings_module = "config.dev"
app = create_app(settings_module)
