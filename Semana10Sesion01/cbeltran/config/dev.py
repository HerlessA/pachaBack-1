# config/dev.py

from .default import *

SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_pass@dev_host:port/db_dev'