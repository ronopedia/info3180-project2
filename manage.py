from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
db = SQLAlchemy(app)
#from app import app 
#from app import db
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Cars(db.Model):
    __tablename__ = 'cars'
  
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    description = db.Column(db.String(100), unique=True, nullable=False)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    colour = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(5), nullable=False)
    transmission = db.Column(db.String(100))
    car_type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    photo = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Favourites(db.Model):
    __tablename__ = 'favourites'
  
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Users(db.Model):
    __tablename__ = 'users'
  
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.String(100))
    photo = db.Column(db.String(50), nullable=False)
    #date_joined = db.Column(db.DateTime(), nullable=False, default=datetime.now)

if __name__ == '__main__':
    manager.run()
