import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy.dialects.postgresql


db = SQLAlchemy()

from mesarument import Measurement


if os.environ['ENV_TYPE'] == 'Development' :
    from config.development import Development as config

if os.environ['ENV_TYPE'] == 'Production' :
    from config.production import Production as config
    




def create_app(conf):
    app = Flask(__name__)
    app.config.from_object(conf)
    db.init_app(app)
    
    return app

app = create_app(config)

migrate = Migrate(app,db)

@app.route("/")
def hello():
    return "Hello world!\n"
