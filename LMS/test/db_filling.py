# skipcq

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from LMS.model.models import Group, User, Student, Course, Tutor

engine = create_engine('postgresql://postgres:@192.168.99.100:54320/postgres', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# first digit - the degree: 1 for Bachelor, 2 for Master, 3 for Specialist
# second digit - the year. 291 group entered in 2019
# third digit - the number of group in this year
group191 = Group(num=191, degree='Bachelor', grade=1)
group281 = Group(num=281, degree='Master', grade=2)

john = User(id=1, name='John', family_name='Smith', verification_code='john12', is_registered=False)
alice = User(id=2, name='Alice', family_name='Turner', verification_code='alice12', email='alice_turner@lms.ru',
             password='AliceTurner1212', middle_name='Sergeevna', is_registered=True)
ann = User(id=3, name='Ann', family_name='Wells', middle_name='Sara', verification_code='ann12',
           email='ann_s_wells@LMS.ru',
           password='AnnWells1212', facebook_link='https://facebook.com/annawells', is_registered=True)
session.add_all([group191, group281, john, alice, ann])

student_john = Student(user_id=john.id, group_num=group191.num, entry_year=2019, is_pay=1)
student_alice = Student(user_id=alice.id, group_num=group191.num, entry_year=2019, is_pay=0)

math_course = Course(id=1, name='Mathematics', description='Introduction into mathematical analysis and linear algebra')
mem_course = Course(id=42, name='Higher Memology', description='The most interesting aspects of modern memes. \
            The basic knowledge of memology is obligatory')
philosophy_course = Course(id=2, name='Philosophy and history of science')

tutor_ann = Tutor(user_id=ann.id, course_id=philosophy_course.id)

session.add_all([student_alice, student_john, tutor_ann, math_course, mem_course, philosophy_course])
session.commit()
