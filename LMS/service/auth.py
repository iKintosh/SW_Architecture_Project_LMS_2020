from LMS.model.models import User
from LMS import db
from flask_jwt_extended import create_access_token
import datetime


def signup(verification_code, email, password):
    user = User.query.filter_by(verification_code=verification_code).first()
    if user is None or user.is_registered is True:
        raise ValueError('User does not exists or already registered')
    user.email = email
    user.password_hash = password
    db.session.add(user)
    db.session.commit()
    u_id = user.id
    return u_id


def login(email, password):
    user = User.query.filter_by(email=email).first()
    if user is None or not user.check_password(password):
        raise ValueError('Invalid email or password')
    expires = datetime.timedelta(days=7)
    access_token = create_access_token(identity=str(user.id), expires_delta=expires)
    return 'Bearer ' + access_token
