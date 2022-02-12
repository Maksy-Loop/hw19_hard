from flask_restx import Resource, Namespace
from flask import jsonify, make_response
from dao.model.user import UserSchema
from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):

    def post(self):
        tokens = auth_service.create_tokens()

        return make_response(jsonify(tokens), 201)

    def put(self):
        tokens = auth_service.create_tokens_with_rt()

        return make_response(jsonify(tokens), 201)





