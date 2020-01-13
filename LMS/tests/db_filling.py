from LMS import db
from flask_login import UserMixin
from LMS import login
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from LMS.models import *

engine = create_engine('postgresql://postgres:@192.168.99.100:54320/postgres', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# first digit - the degree: 1 for Bachelor, 2 for Master, 3 for Specialist
# second digit - the year. 291 group entered in 2019
# third digit - the number of group in this year
group1 = Group(num=191, degree='Bachelor', grade=1)
group2 = Group(num=281, degree='Master', grade=2)

john = User(name='John', family_name='Smith', verification_code='john123')
alice = User(name='Alice', family_name='Turner', verification_code='alice123', email='alice_turner@lms.ru', \
             password_hash='AliceTurner1212', middle_name='Sergeevna')
'''
student_john = Student(user_id=john.id, group_num=group1.num, entity_year=2019)

math_course = Course(id=1, name='Mathematics', decription='Introduction into mathematical analysis and linear algebra')
mem_course = Course(id=42, name='Higher Memology', description='The most interesting aspects of modern memes. \
            The basic knowledge of memology is obligatory'



'''
session.add(alice)
session.commit()
