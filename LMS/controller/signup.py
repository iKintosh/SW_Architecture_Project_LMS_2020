from flask_restplus import Namespace, Resource, fields, abort
from http import HTTPStatus
from LMS.service import auth

api = Namespace('signup', description='sign up')

SignupItem = api.parser()
SignupItem.add_argument('verification_code', type=str, help='verification code provided by admin', required=True)
SignupItem.add_argument('email', type=str, help='Your email', required=True)
SignupItem.add_argument('password', type=str, help='Your password; make sure it is at least 6 symbols', required=True)

user_id = api.model('NewUser', {
    'id': fields.Integer
})


@api.route('')
class SignupApi(Resource):
    @api.expect(SignupItem)
    @api.response(HTTPStatus.BAD_REQUEST, 'Validation error')
    @api.marshal_with(user_id, code=HTTPStatus.CREATED, description='User registered')
    def post(self):
        args = SignupItem.parse_args()
        try:
            auth.signup(**args)
        except ValueError as e:
            abort(HTTPStatus.BAD_REQUEST, message=str(e))
        return {'id': 12}, HTTPStatus.CREATED
