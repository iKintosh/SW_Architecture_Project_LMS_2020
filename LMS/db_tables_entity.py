from sqlalchemy import Column, Integer, String, DateTime
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
