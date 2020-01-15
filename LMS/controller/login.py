from http import HTTPStatus

from flask_restplus import Namespace, Resource, fields, abort
from LMS.service import auth

api = Namespace('login', description='login')

LoginItem = api.parser()
LoginItem.add_argument('email', type=str, help='Your email', required=True)
LoginItem.add_argument('password', type=str, help='Your password', required=True)

login_token = api.model('AuthToken', {
    'token': fields.String
})


@api.route('')
class LoginApi(Resource):
    @api.expect(LoginItem)
    @api.response(HTTPStatus.BAD_REQUEST, 'Validation error')
    @api.marshal_with(login_token, code=HTTPStatus.ACCEPTED, description='Login')
    def post(self):
        args = LoginItem.parse_args()
        try:
            token = auth.login(**args)
        except ValueError as e:
            abort(HTTPStatus.BAD_REQUEST, message=str(e))
        return {'token': token}, HTTPStatus.ACCEPTED
