from flask import request
from flask_restful import Resource
from Model import db, Profile, ProfileSchema

profiles_schema = ProfileSchema(many=True)
profile_schema = ProfileSchema()

class ProfileResource(Resource):
    def get(self):
        profiles = Profile.query.all()
        profiles = profiles_schema.dump(profiles).data
        usersdata={}
        for users in profiles:
            usersdata[users['id']]=users
        return {'status': 'success', 'data': usersdata}, 200    

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = profile_schema.load(json_data)

        if errors:
            return errors, 422
        user = Profile.query.filter_by(name=data['name'],mobile=json_data['mobile'],
            email=json_data['email'],username=json_data['username']).first()

        if user:
            return {'message': 'user already exists'}, 400
        user = Profile(
            name=json_data['name'],
            mobile=json_data['mobile'],
            country=json_data['country'],
            email=json_data['email'],
            username=json_data['username'],
            password=json_data['password'],
            )
        db.session.add(user)
        db.session.commit()
        result = profile_schema.dump(user).data
        return { "status": 'success', 'data': result }, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = profile_schema.load(json_data)

        if errors:
            return errors, 422
        user = Profile.query.filter_by(id=data['id']).first()

        if not user:
            return {'message': 'user does not exist'}, 400
        user.name = data['name']
        user.mobile=data['mobile']
        user.country=data['country']
        user.email=data['email']
        user.username=data['username']
        user.password=data['password']
        
        db.session.commit()
        result = profile_schema.dump(user).data
        return { "status": 'success', 'data': result }, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = profile_schema.load(json_data)

        if errors:
            return errors, 422
        user = Profile.query.filter_by(id=data['id']).delete()
        db.session.commit()
        result = profile_schema.dump(user).data
        return { "status": 'success', 'data': result}, 204