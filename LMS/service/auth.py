from LMS.model.models import User
from LMS import db


def signup(verification_code, email, password):
    user = User.query.filter_by(verification_code=verification_code).first()
    if user is None or user.is_registered is True:
        raise ValueError('User does not exists or already registered')
    user = User(email=email, password_hash=password)
    db.session.add(user)
    db.session.commit()
    u_id = user.id
    return u_id
