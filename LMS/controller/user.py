from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_restplus import Namespace
from flask_restplus import Resource

from LMS.controller.signup import USER_ID
from LMS.service import user_services

API = Namespace("user", description="User")

AUTH_HEADER = API.parser()
AUTH_HEADER.add_argument("Authorization", location="headers")


@API.route("")
class UserListAPI(Resource):
    """User API"""

    @jwt_required
    @API.doc("Get list of groupmates")
    @API.expect(AUTH_HEADER)
    @API.response(HTTPStatus.UNAUTHORIZED, "Auth error")
    @API.marshal_list_with(
        USER_ID, code=HTTPStatus.OK, description="List of groupmates"
    )
    def get(self):
        u_id = get_jwt_identity()
        groupmates = user_services.get_groupmates(u_id)
        return groupmates, HTTPStatus.OK


@API.route("/<int:url_id>")
class UserAPI(Resource):
    @jwt_required
    @API.doc("Get profile")
    @API.expect(AUTH_HEADER)
    @API.response(HTTPStatus.UNAUTHORIZED, "Auth error")
    @API.response(HTTPStatus.OK, "Profile info")
    def get(self, url_id):
        u_id = get_jwt_identity()
        profile = user_services.get_profile(url_id, u_id)
        return profile, HTTPStatus.OK


"""@API.route('/<user>/<courses>')
class UserCoursesApi(Resource):
    @jwt_required
    @API.doc('Get my courses list')
    @API.expect(AUTH_HEADER)
    @API.response(HTTPStatus.UNAUTHORIZED, 'Auth error')
    @API.marshal_with(USER_ID, code=HTTPStatus.OK, description='Get my courses list')
    def get(self):
        u_id = get_jwt_identity()
        courses = user_services.get_my_courses(u_id)
        return courses, HTTPStatus.OK"""
