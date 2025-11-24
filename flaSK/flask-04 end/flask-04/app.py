from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from psycopg2_connect import connect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///theme_04.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.String, nullable=False)

conn = connect(user, host, port, database, password)



