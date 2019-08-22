from flask import request
from flask_restful import Resource
from Model import db, Wallet, WalletSchema

wallets_schema = WalletSchema(many=True)
wallet_schema = WalletSchema()

class WalletResource(Resource):
    def get(self):
        wallets = Wallet.query.all()
        wallets = wallets_schema.dump(wallets).data
        userwallets={}
        for userwallet in wallets:
            userwallets[userwallet['id']]=userwallet
        return {'status': 'success', 'data': userwallets}, 200    

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = wallet_schema.load(json_data)

        if errors:
            return errors, 422
        userwallet = Wallet.query.filter_by(profile_id=data['profile_id']).first()

        if userwallet:
            return {'message': "user wallet exist already"}, 400
        userwallet = Wallet(
            profile_id=json_data['profile_id'],
            total_balance=json_data['total_balance'],
            list_of_coin=json_data['list_of_coin']
        )
        db.session.add(userwallet)
        db.session.commit()
        result = wallet_schema.dump(userwallet).data
        return { 'status': 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_jason(force=True)
        if not json_data:
            return {'message': 'data is not json'}, 400
        data, errors = wallet_schema.load(json_data)

        if errors:
            return errors, 422
        userwallet = Wallet,query.filter_by(profile_id=data['profile_id'])

        if not userwallet:
            return {'message': 'userwallet does not exist'}
        userwallet.total_balance=data['total_balance']
        userwallet.list_of_coin=data['list_of_coin']
        db.session.commit()
        result = wallet_schema.dump(userwallet).data
        return  {'status': 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = wallet_schema.load(json_data)

        if errors:
            return errors, 422
        userwallet = Wallet.query.filter_by(profile_id=data['profile_id']).delete()
        db.session.commit()
        result = wallet_schema.dump(user).data
        return { "status": 'success', 'data': result}, 204
