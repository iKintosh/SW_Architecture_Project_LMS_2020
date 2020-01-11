from LMS import db
from flask_login import UserMixin
from LMS import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    family_name = db.Column(db.String)
    status = db.Column(db.String)
    verification_code = db.Column(db.String)
    email = db.Column(db.String)
    password_hash = db.Column(db.String)
    phone = db.Column(db.String)

    def __repr__(self):
        return f"<User(name={self.name}, family_name={self.family_name}, status={self.status}," \
               f"email={self.email}, phone={self.phone})>"


class Group(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String)
    grade = db.Column(db.Integer)
    students = db.relationship('Student', backref='group', lazy='dynamic')

    def __repr__(self):
        return f"<User(num={self.num}, degree={self.degree}, grade={self.grade})>"


class Student(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    group_num = db.Column(db.Integer, db.ForeignKey('group.num'))
    pay_flg = db.Column(db.Boolean)

    def __repr__(self):
        return "<User(name='%s', group_number='%d')>" % (User.name, self.group_num)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    materials = db.relationship('Material', backref='course', lazy='dynamic')
    homeworks = db.relationship('Homework', backref='course', lazy='dynamic')

    def __repr__(self):
        return f"<User(name={self.name}, description={self.description})>"


class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    text = db.Column(db.String)
    date = db.Column(db.DateTime)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __repr__(self):
        return "<User(name='%s', name='%s', 'text'='%s')>" % (
            self.name, self.name, self.text)


class Homework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    valid_from = db.Column(db.DateTime)
    valid_to = db.Column(db.DateTime)
    description = db.Column(db.String)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __repr__(self):
        return f"<Homework(name={self.name}, valid_from={self.valid_from}, valid_to={self.valid_to}," \
               f"description={self.description}, course_id={self.course_id})>"


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String)
    submit_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Answer(answer={self.answer}, submit_date={self.submit_date})>"


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
