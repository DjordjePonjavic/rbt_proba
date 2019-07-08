from . import Config as Config

class Development(Config):
    EVN_TYPE = "Dev"

    DB_NAME = "temperature"
    DB_USER =  "ognjen"
    DB_PASSWD = "praksa"
    DB_HOST = "127.0.0.1"
    DB_PORT = 5432

    pass
