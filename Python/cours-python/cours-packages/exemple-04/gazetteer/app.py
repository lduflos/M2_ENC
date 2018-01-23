from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from .routes import lieu, accueil : s'il avait été placé là, il y aurait eu une boucle entre fichiers app et routes

app = Flask("Application")
# On configure la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://gazetteer_user:password@localhost/gazetteer'
# On initie l'extension
db = SQLAlchemy(app)

from .routes import lieu, accueil
