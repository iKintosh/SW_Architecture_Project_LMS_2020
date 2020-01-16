from http import HTTPStatus

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restplus import Namespace, Resource, fields

from LMS.service import user_services
from LMS.controller.signup import user_id

api = Namespace('user', description='User')

AuthHeader = api.parser()
AuthHeader.add_argument('Authorization', location='headers')


@api.route('')
class UserListAPI(Resource):
    """User API"""

    @jwt_required
    @api.doc('Get list of groupmates')
    @api.expect(AuthHeader)
    @api.response(HTTPStatus.UNAUTHORIZED, 'Auth error')
    @api.marshal_list_with(user_id, code=HTTPStatus.OK, description='List of groupmates')
    def get(self):
        u_id = get_jwt_identity()
        groupmates = user_services.get_groupmates(u_id)
        return groupmates, HTTPStatus.OK


@api.route('/<int:id>')
class UserAPI(Resource):
    @jwt_required
    @api.doc('Get profile')
    @api.expect(AuthHeader)
    @api.response(HTTPStatus.UNAUTHORIZED, 'Auth error')
    # @api.marshal_with(user_id, code=HTTPStatus.OK, description='List of groupmates')
    def get(self, id):
        u_id = get_jwt_identity()
        profile = user_services.get_profile(id, u_id)
        return {}, 200