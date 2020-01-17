from http import HTTPStatus

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restplus import Namespace, Resource

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


@api.route('/<int:url_id>')
class UserAPI(Resource):
    @jwt_required
    @api.doc('Get profile')
    @api.expect(AuthHeader)
    @api.response(HTTPStatus.UNAUTHORIZED, 'Auth error')
    @api.response(HTTPStatus.OK, 'Profile info')
    def get(self, url_id):
        u_id = get_jwt_identity()
        profile = user_services.get_profile(url_id, u_id)
        return profile, HTTPStatus.OK


'''@api.route('/<user>/<courses>')
class UserCoursesApi(Resource):
    @jwt_required
    @api.doc('Get my courses list')
    @api.expect(AuthHeader)
    @api.response(HTTPStatus.UNAUTHORIZED, 'Auth error')
    @api.marshal_with(user_id, code=HTTPStatus.OK, description='Get my courses list')
    def get(self):
        u_id = get_jwt_identity()
        courses = user_services.get_my_courses(u_id)
        return courses, HTTPStatus.OK'''
