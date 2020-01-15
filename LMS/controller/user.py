from flask_jwt_extended import jwt_required
from flask_restplus import Namespace, Resource, fields

api = Namespace('user', description='User')

UserItem = api.parser()
UserItem.add_argument('name', type=str, help='Some param')
UserItem.add_argument('Authorization', location='headers')


@api.route('')
class UserList(Resource):
    """User API"""

    @api.doc('User API')
    @api.expect(UserItem)
    @jwt_required
    def post(self):
        data = UserItem.parse_args()
        print(data)
        return {}, 200
