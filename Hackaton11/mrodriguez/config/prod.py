# config propia de producción

from .default import *

from dotenv import load_dotenv
import os

load_dotenv()
ELEPHANT_URI = os.environ["ELEPHANT_URI"]

SQLALCHEMY_DATABASE_URI = f"{ELEPHANT_URI}"
