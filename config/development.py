from . import Config as Config

class Development(Config):
    
    ENV_TYPE = "Dev"
    DB_NAME = "praksa_19"
    DB_USER =  "djoleksa"
    DB_PASSWD = "sakalaka;"
    DB_HOST = "127.0.0.1"
    DB_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    

    SQLALCHEMY_DATABASE_URI = \
        f'postgresql+psycopg2://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


    