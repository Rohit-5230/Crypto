from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy, BaseQuery

ma = Marshmallow()
db = SQLAlchemy()

#PROFILE
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    #created = db.Column(db.DataTime())

    name = db.Column(db.String(20),unique=True, nullable=False)
    mobile = db.Column(db.String(10), unique=True, nullable=False)
    country = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, name, mobile, country, email, username, password):
        self.name = name
        self.mobile = mobile
        self.country = country
        self.email = email
        self.username = username
        self.password = password
    
class ProfileSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    mobile = fields.String(required=True)
    country = fields.String(required=True)
    email = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    
#WALLET
class Wallet(db.Model):
    __tablename__ = 'wallets'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id', onupdate='CASCADE', ondelete='CASCADE'))
    profiles = db.relationship("Profile", backref=db.backref("profiles", uselist=False))

    total_balance = db.Column(db.Integer)
    list_of_coin = db.Column(db.String())

    def __init__(self, profile_id, total_balance, list_of_coin):
        self.profile_id = profile_id
        self.total_balance = total_balance
        self.list_of_coin = list_of_coin

class WalletSchema(ma.Schema):
    id = fields.Integer()
    profile_id = fields.Integer()
    total_balance = fields.Integer()
    list_of_coin = fields.String(required=True)



    

