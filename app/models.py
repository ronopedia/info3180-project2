from . import db
from werkzeug.security import generate_password_hash


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
  date_joined = db.Column(db.DateTime, nullable=False, default=datetime.now)
  
  def __init__(self, username, password, name, email, location, biography, photo, date_joined):
    self.username = username
    self. password = generate_password_hash(password, method='pbkdf2:sha256')
    self.name = name
    self. email = email
    self.location = location
    self.biography = biography
    self.photo = photo
    self.date_joined = datetime.now()
    
  def __repr__(self):
    return '<User %r>' % (self.username)  
  

class Favourites(db.Model):
  __tablename__ = 'favourites'
  
  id = db.Column(db.Integer, primary_key=True, autoincrement = True)
  car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  
  def __init__(self, car_id, user_id):
    self.car_id = car_id
    self.user_id = user_id
  
  def __repr__(self):
    return '<Favourite %r>' % (self.car_id) 
        
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
  price = db.Column(db.Decimal(10,2), nullable=False)
  photo = db.Column(db.String(50), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  
  def __init__(self, description, make, model, colour, year, transmission, car_type, price, photo, user_id):
    self.description = description
    self.make = make
    self.model = model
    self.colour = colour
    self.year = year
    self.transmission = transmission
    self.car_type = car_type
    self.price = price
    self.photo = photo
    self.user_id = user_id
    
  def __repr__(self):
    return '<Car: %r %r %r %r %r>' % (self.colour, self.make, self.model, self.car_type, self.price)
   
#def is_authenticated(self):
#  return True

#def is_active(self):
#  return True

#def is_anonymous(self):
#  return False
  
  
  
