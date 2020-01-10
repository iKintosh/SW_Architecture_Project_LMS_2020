from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    family_name = Column(String)
    status = Column(String)
    verification_code = Column(String)
    email = Column(String)
    phone = Column(String)

    def __repr__(self):
        return f"<User(name={self.name}, family_name={self.family_name}, status={self.status}," \
               f"email={self.email}, phone={self.phone})>"


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __repr__(self):
        return "<User(name='%s', description='%s')>" % (
            self.name, self.description)


class Group(Base):
    __tablename__ = 'groups'

    num = Column(Integer, primary_key=True)
    degree = Column(String)
    grade = Column(Integer)

    def __repr__(self):
        return "<User(num='%d', degree='%s', grade='%d')>" % (
            self.num, self.degree, self.grade)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    group_num = Column(Integer, ForeignKey('groups.num'))
    pay_flg = Column(Boolean)

    def __repr__(self):
        return "<User(name='%s', group_number='%d')>" % (
            User.name, self.group_num)


class Material(Base):
    __tablename__ = 'materials'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    name = Column(String)
    text = Column(String)
    date = Column(DateTime)
    course_id = Column(Integer, ForeignKey('courses.id'))

    def __repr__(self):
        return "<User(name='%s', name='%s', 'text'='%s')>" % (
            self.name, self.name, self.text)


class Homework(Base):
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    valid_from = Column(DateTime)
    valid_to = Column(DateTime)
    description = Column(String)
    course_id = Column(Integer)

    def __repr__(self):
        return f"<Homework(name={self.name}, valid_from={self.valid_from}, valid_to={self.valid_to}," \
               f"description={self.description}, course_id={self.course_id})>"


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    answer = Column(String)
    submit_date = Column(DateTime)

    def __repr__(self):
        return f"<Answer(answer={self.answer}, submit_date={self.submit_date})>"


def get_base_class():
    return Base
