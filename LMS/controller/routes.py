from LMS import api
from LMS.controller import login
from LMS.controller import signup
from LMS.controller import user

api.add_resource(signup.SignupApi, "/signup")
api.add_resource(login.LoginApi, "/login")
api.add_resource(user.UserListAPI, "/user")
api.add_resource(user.UserAPI, "/user/<int:url_id>")
"""api.add_resourse(user.UserCoursesApi, '/user/courses')
"""
