from LMS import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    family_name = db.Column(db.String)
    middle_name = db.Column(db.String)

    is_tutor = db.Column(db.Boolean)
    is_moderator = db.Column(db.Boolean)

    verification_code = db.Column(db.String)
    is_registered = db.Column(db.Boolean, default=False)
    email = db.Column(db.String)
    password_hash = db.Column(db.String)

    phone = db.Column(db.String)
    city = db.Column(db.String)
    about_me = db.Column(db.String)
    vk_link = db.Column(db.String)
    facebook_link = db.Column(db.String)
    linkedin_link = db.Column(db.String)
    instagram_link = db.Column(db.String)

    def __repr__(self):
        return f"<User(name={self.name}, family_name={self.family_name}, status={self.status}," \
               f"email={self.email}, phone={self.phone})>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Group(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String)
    grade = db.Column(db.Integer)
    students = db.relationship('Student', backref='group', lazy='dynamic')

    def __repr__(self):
        return f"<Group(num={self.num}, degree={self.degree}, grade={self.grade})>"


class Tutor(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)


class Moderator(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)


class Student(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    group_num = db.Column(db.Integer, db.ForeignKey('group.num'), primary_key=True)
    entry_year = db.Column(db.Integer)
    is_pay = db.Column(db.Boolean)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    tutors = db.relationship('Tutor', backref='course', lazy='dynamic')
    moderators = db.relationship('Moderator', backref='course', lazy='dynamic')
    materials = db.relationship('Material', backref='course', lazy='dynamic')
    homeworks = db.relationship('Homework', backref='course', lazy='dynamic')

    def __repr__(self):
        return f"<Course(name={self.name}, description={self.description})>"


class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    text = db.Column(db.String)
    date = db.Column(db.DateTime)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __repr__(self):
        return "<Material(name='%s', name='%s', 'text'='%s')>" % (
            self.name, self.name, self.text)


class Homework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    valid_from = db.Column(db.DateTime)
    valid_to = db.Column(db.DateTime)
    description = db.Column(db.String)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    answers = db.relationship('Answer', backref='homework', lazy='dynamic')

    def __repr__(self):
        return f"<Homework(name={self.name}, valid_from={self.valid_from}, valid_to={self.valid_to}," \
               f"description={self.description}, course_id={self.course_id})>"


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    homework_id = db.Column(db.Integer, db.ForeignKey('homework.id'))
    answer = db.Column(db.String)
    submit_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Answer(answer={self.answer}, submit_date={self.submit_date})>"
