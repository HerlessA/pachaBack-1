# config propia de desarrollo
from .default import *

from dotenv import load_dotenv
import os

load_dotenv()
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

TESTING = False
DEBUG = True

SQLALCHEMY_DATABASE_URI = (
    f"postgresql://postgres:{POSTGRES_PASSWORD}@localhost:5432/minimarket"
)
