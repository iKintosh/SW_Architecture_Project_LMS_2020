from LMS.model.models import Course
from LMS.model.models import Curriculum
from LMS.model.models import Group
from LMS.model.models import Student
from LMS.model.models import Tutor
from LMS.model.models import User


def get_groupmates(u_id):
    """get list of groupmates id"""
    user = (User.query.join(Student).filter(User.id == u_id).add_columns(
        Student.group_num).first())
    group_num = user.group_num
    students = Group.query.filter_by(num=group_num).first().students.all()
    students_id = []
    for S in students:
        students_id.append({"url_id": S.user_id})
    return students_id


def get_profile(request_id, u_id):
    """get profile info"""
    user = User.query.filter_by(id=request_id).first()
    student = Student.query.filter_by(user_id=request_id).first()
    group = Group.query.filter_by(num=student.group_num).first()
    profile = {
        "full name":
        (user.name + " " + user.middle_name + " " + user.family_name),
        "e-mail": user.email,
        "phone number": user.phone,
        "home city": user.city,
        "about me": user.about_me,
        "vk": user.vk_link,
        "instagram": user.instagram_link,
        "facebook": user.facebook_link,
        "LinkedIn": user.linkedin_link,
    }
    if student.user_id is not None:
        profile.update({
            "status": "student",
            "group": student.group_num,
            "degree": group.degree,
            "grade": group.grade,
        })
        if request_id == u_id:
            profile.update({"pay uni": student.is_pay})
    else:
        profile.update({"status": "tutor"})
    return profile


def get_my_courses(u_id):
    """get list of courses id, that user with u_id attends"""
    student = Student.query.filter_by(user_id=u_id).first()
    tutor = Tutor.query.filter_by(user_id=u_id).first().tutor.all()
    courses_ids = []
    if student is not None:
        group_num = student.group_num
        courses = Curriculum.query.filter_by(group_num=group_num)
        for course in courses:
            courses_ids.append({"course_id": course.id})
    elif tutor is not None:
        for T in tutor:
            courses_ids.append({"course_id": T.course_id})
    return courses_ids


def change_password(u_id, old_password, new_password):
    """change password"""
    user = User.query.filter_by(id=u_id).first()
    if user.check_password(old_password):
        user.password = new_password


def get_course(c_id):
    """get course info"""
    course = Course.query.filter_by(id=c_id)
    c_profile = {
        "name": course.name,
        "description": course.description,
        "tutors": course.tutors,
        "moderators": course.moderators,
        "materials": course.materials,
        "homeworks": course.homeworks,
    }
    return c_profile
