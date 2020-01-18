from LMS import db
from flask_login import UserMixin
from LMS import login
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from LMS.models import *
import datetime as dt

engine = create_engine(
    'postgresql://postgres:@192.168.99.100:54320/postgres', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# first digit - the degree: 1 for Bachelor, 2 for Master, 3 for Specialist
# second digit - the year. 291 group entered in 2019
# third digit - the number of group in this year
group191 = Group(num=191, degree='Bachelor', grade=1)
group281 = Group(num=281, degree='Master', grade=2)

john = User(id=1, name='John', family_name='Smith', verification_code='john12')
alice = User(id=2, name='Alice', family_name='Turner', verification_code='alice12', email='alice_turner@lms.ru',
             password_hash='AliceTurner1212', middle_name='Sergeevna')
ann = User(id=3, name='Ann', family_name='Wells', middle_name='Sara', verification_code='ann12',
           email='ann_s_wells@LMS.ru', password_hash='AnnWells1212', facebook_link='https://facebook.com/annawells')

student_john = Student(
    user_id=john.id, group_num=group191.num, entry_year=2019, is_pay=1)
student_alice = Student(
    user_id=alice.id, group_num=group191.num, entry_year=2019, is_pay=0)

math_course = Course(id=1, name='Mathematics',
                     description='Introduction into mathematical analysis and linear algebra')
mem_course = Course(id=42, name='Higher Memology', description='The most interesting aspects of modern memes. \
            The basic knowledge of memology is obligatory')
philosophy_course = Course(id=2, name='Philosophy and history of science')

tutor_ann = Tutor(user_id=ann.id, course_id=philosophy_course.id)

Kant_philosophy = Material(id=1, name='Kants conception of philosophy', text='some text about Kant',
                           date=dt.datetime(2019, 11, 1, 10, 10, 00), course_id=philosophy_course.id)
Matrix_math = Material(id=2, name='Matrixes and matrix operations', text='some math matrix blablabla difficult',
                       date=dt.datetime(2019, 11, 25, 10, 10, 00), course_id=math_course.id)
Integral_math = Material(id=3, name='Integrals', text='something(x) dx = F(something(x))',
                         date=dt.datetime(2019, 11, 10, 10, 00, 00), course_id=math_course.id)

homework_matrix = Homework(id=1, name='Practice in matrix operations',
                           valid_from=dt.datetime(2019, 11, 29, 10, 00, 00),
                           valid_to=dt.datetime(2019, 12, 1, 10, 00, 00),
                           description='AX=b, X=?', course_id=math_course.id)
homework1_philosophy = Homework(id=2, name='Your fist philosophical essay',
                                valid_from=dt.datetime(
                                    2019, 11, 29, 10, 10, 00),
                                valid_to=dt.datetime(2019, 12, 15, 19, 00, 00),
                                description='Write an essay on philosophical topic', course_id=philosophy_course.id)
john_answer_philosophy = Answer(id=1, user_id=john.id, homework_id=homework1_philosophy.id, answer='John\'s essay',
                                submit_date=dt.datetime(2019, 12, 11, 9, 00, 00))
alice_answer_philosophy = Answer(id=2, user_id=alice.id, homework_id=homework1_philosophy.id,
                                 answer='To be or not to be, that\'s the question is',
                                 submit_date=dt.datetime(2019, 12, 2, 18, 1, 00))

group281_x_philosophy = Curriculum(
    course_id=philosophy_course.id, group_num=group281.num)
group191_x_philosophy = Curriculum(
    course_id=philosophy_course.id, group_num=group191.num)
group191_x_math = Curriculum(course_id=math_course.id, group_num=group191.num)

session.add_all([group191, group281, john, alice, ann])
session.commit()
session.add_all([student_alice, student_john, tutor_ann,
                 math_course, mem_course, philosophy_course, Kant_philosophy])
session.commit()
session.add_all([Matrix_math, Integral_math, homework1_philosophy,
                 homework_matrix, john_answer_philosophy])
session.commit()
session.add_all([alice_answer_philosophy, group191_x_math,
                 group191_x_philosophy, group281_x_philosophy])
session.commit()
