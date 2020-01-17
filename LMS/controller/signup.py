from http import HTTPStatus

from flask_restplus import abort
from flask_restplus import fields
from flask_restplus import Namespace
from flask_restplus import Resource

from LMS.service import auth

API = Namespace("signup", description="sign up")

SIGNUP_ITEM = API.parser()
SIGNUP_ITEM.add_argument(
    "verification_code",
    type=str,
    help="verification code provided by admin",
    required=True,
)
SIGNUP_ITEM.add_argument("email", type=str, help="Your email", required=True)
SIGNUP_ITEM.add_argument(
    "password",
    type=str,
    help="Your password; make sure it is at least 6 symbols",
    required=True,
)

USER_ID = API.model("User", {"url_id": fields.Integer})


@API.route("")
class SignupApi(Resource):
    @API.expect(SIGNUP_ITEM)
    @API.response(HTTPStatus.BAD_REQUEST, "Validation error")
    @API.marshal_with(USER_ID, code=HTTPStatus.CREATED, description="User registered")
    def post(self):
        args = SIGNUP_ITEM.parse_args()
        try:
            new_user_id = auth.signup(**args)
        except ValueError as e:
            abort(HTTPStatus.BAD_REQUEST, message=str(e))
        return {"url_id": new_user_id}, HTTPStatus.CREATED
