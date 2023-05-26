# config/dev.py

from .default import *

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pacha23@localhost:5432/miniblog'
