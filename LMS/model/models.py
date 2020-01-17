from LMS import db
from werkzeug.security import generate_password_hash, check_password_hash

PHONE_LENGTH = 12


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    family_name = db.Column(db.String, nullable=False)
    middle_name = db.Column(db.String)

    is_tutor = db.Column(db.Boolean)
    is_moderator = db.Column(db.Boolean)

    verification_code = db.Column(db.String, unique=True, nullable=False)
    is_registered = db.Column(db.Boolean, default=False)
    email = db.Column(db.String, unique=True)

    __password_hash = db.Column(db.String)

    @property
    def password(self):
        return self.__password_hash

    @password.setter
    def password(self, password):
        self.__password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.__password_hash, password)

    __phone = db.Column(db.String)

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if value[:2] == "+7" and len(value) == PHONE_LENGTH:
            self.__phone = value
        else:
            raise ValueError("Phone format is wrong. Use +7... format")

    city = db.Column(db.String)
    about_me = db.Column(db.String)

    __vk_link = db.Column(db.String)

    @property
    def vk_link(self):
        return self.__vk_link

    @vk_link.setter
    def vk_link(self, value):
        if value.startswith("https://vk.com/"):
            self.__vk_link = value
        else:
            raise ValueError("Link format is wrong. Use https://vk.com/ format")

    __facebook_link = db.Column(db.String)

    @property
    def facebook_link(self):
        return self.__facebook_link

    @facebook_link.setter
    def facebook_link(self, value):
        if value.startswith("https://facebook.com/"):
            self.__facebook_link = value
        else:
            raise ValueError("Link format is wrong. Use https://facebook.com/ format")

    __linkedin_link = db.Column(db.String)

    @property
    def linkedin_link(self):
        return self.__linkedin_link

    @linkedin_link.setter
    def linkedin_link(self, value):
        if value.startswith("https://linkedin.com/"):
            self.__linkedin_link = value
        else:
            raise ValueError("Link format is wrong. Use https://linkedin.com/ format")

    __instagram_link = db.Column(db.String)

    @property
    def instagram_link(self):
        return self.__instagram_link

    @instagram_link.setter
    def instagram_link(self, value):
        if value.startswith("https://www.instagram.com/"):
            self.__instagram_link = value
        else:
            raise ValueError(
                "Link format is wrong. Use https://www.instagram.com/ format"
            )

    def __repr__(self):
        return (
            f"<User(name={self.name}, family_name={self.family_name},"
            f"email={self.email}, phone={self.phone})>"
        )


class Group(db.Model):
    num = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    students = db.relationship("Student", backref="group", lazy="dynamic")

    def __repr__(self):
        return f"<Group(num={self.num}, degree={self.degree}, grade={self.grade})>"


class Tutor(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.url_id"), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.url_id"), primary_key=True)


class Moderator(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.url_id"), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.url_id"), primary_key=True)


class Student(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.url_id"), primary_key=True)
    group_num = db.Column(db.Integer, db.ForeignKey("group.num"), primary_key=True)
    entry_year = db.Column(db.Integer, nullable=False)
    is_pay = db.Column(db.Boolean)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    tutors = db.relationship("Tutor", backref="course", lazy="dynamic")
    moderators = db.relationship("Moderator", backref="course", lazy="dynamic")
    materials = db.relationship("Material", backref="course", lazy="dynamic")
    homeworks = db.relationship("Homework", backref="course", lazy="dynamic")

    def __repr__(self):
        return f"<Course(name={self.name}, description={self.description})>"


class Curriculum(db.Model):
    course_id = db.Column(db.Integer, db.ForeignKey("course.url_id"), primary_key=True)
    group_num = db.Column(db.Integer, db.ForeignKey("group.num"), primary_key=True)


class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    text = db.Column(db.String)
    date = db.Column(db.DateTime)
    course_id = db.Column(db.Integer, db.ForeignKey("course.url_id"))

    def __repr__(self):
        return "<Material(name='%s', name='%s', 'text'='%s')>" % (
            self.name,
            self.name,
            self.text,
        )


class Homework(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    valid_from = db.Column(db.DateTime)
    valid_to = db.Column(db.DateTime)
    description = db.Column(db.String)
    course_id = db.Column(db.Integer, db.ForeignKey("course.url_id"))
    answers = db.relationship("Answer", backref="homework", lazy="dynamic")

    def __repr__(self):
        return (
            f"<Homework(name={self.name}, valid_from={self.valid_from}, valid_to={self.valid_to},"
            f"description={self.description}, course_id={self.course_id})>"
        )


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.url_id"))
    homework_id = db.Column(db.Integer, db.ForeignKey("homework.url_id"))
    answer = db.Column(db.String)
    submit_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Answer(answer={self.answer}, submit_date={self.submit_date})>"
