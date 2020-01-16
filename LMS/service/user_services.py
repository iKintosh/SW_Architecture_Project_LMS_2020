from LMS.model.models import User, Group, Student


def get_groupmates(u_id):
    user = User.query.join(Student).filter(User.id == u_id).add_columns(Student.group_num).first()
    group_num = user.group_num
    students = Group.query.filter_by(num=group_num).first().students.all()
    students_id = []
    for s in students:
        students_id.append({'id': s.user_id})
    return students_id


def get_profile(id, u_id):
    user = User.query.filter_by(id=id).first()
    # собрать данные о пользователе, если id и u_id совпадают, то выдать информацию и по оплате обучения,
    # иначе только общедоступную
    return None
