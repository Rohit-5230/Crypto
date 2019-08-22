from flask import Blueprint
from flask_restful import Api
from resources.profile import ProfileResource
from resources.wallet import WalletResource

api_bp = Blueprint('api',__name__) 
api = Api(api_bp)

#Route
api.add_resource(ProfileResource, '/Profile')
api.add_resource(WalletResource, '/Wallet')
