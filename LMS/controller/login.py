from flask_restplus import Namespace, Resource

api = Namespace('login', description='login')

LoginItem = api.parser()
LoginItem.add_argument('email', type=str, help='Your email', required=True)
LoginItem.add_argument('password', type=str, help='Your password; make sure it is at least 6 symbols', required=True)


@api.route('')
class LoginApi(Resource):
    @api.expect(LoginItem)
    def post(self):
        pass
