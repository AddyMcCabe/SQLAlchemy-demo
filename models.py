import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.abspath(os.path.dirname(__file__))

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Viking(db.model):

    __tablename__ = 'vikings'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # ONE TO MANY
    # Viking to Many Weapons...
    weapons = db.relationship('Weapon', backref='viking', lazy='dynamic')
    # ONE TO ONE
    #  ONE VIKING -- ONE PET
    pet = db.relationship('Pet', backref='viking', uselist=False)


    def __init__(self, name):
        self.name = name

    def __reprz__(self):
        if self.owner:
            return f"Owners name is {self.name} and the pet is {self.pet.name}"
        else:
            return f"Vikings name is {self.name} and has no pet yet."

    def report_weapons(self):
        print("Here are my weapons:")
        for weapon in self.weapons:
            print(weapon.item_name)

class Weapons(db.model):
    __tablename__ = 'weapons'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    viking_id = db.Column(db.Integer, db.ForeignKey('vikings.id'))

    def __init__(self, item_name, viking_id):
        self.item_name = item_name
        self.viking_id = viking_id

class Pet(db.model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    viking_id = db.Column.(db.Integer, db.ForiegnKey('vikings.id'))

    def __init__(self, name, viking_id):
        self.name = name
        self.viking_id = viking_id