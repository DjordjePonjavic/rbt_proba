import os
from config import Config
class Production(Config):
    ENV_TYPE = "Production"
    SQL_ALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']