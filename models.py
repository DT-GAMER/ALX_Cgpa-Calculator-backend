from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    courses = db.relationship('Course', backref='user', lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(20), nullable=False)
    course_title = db.Column(db.String(100), nullable=False)
    course_unit = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    user_id = db.Column(db.Integer, d<F11><F11>b.ForeignKey('users.id'), nullable=False)

    def __init__(self, course_code, course_title, course_unit, grade, user_id):
        self.course_code = course_code
        self.course_title = course_title
        self.course_unit = course_unit
        self.grade = grade
        self.user_id = user_id

    def calculate_grade_point(self):   
        # Define your logic to calculate the grade point based on the grade
        # Return the calculated grade point

        # Example implementation:
        if self.grade == 'A':
            return 5.0
        elif self.grade == 'B':
            return 4.0
        elif self.grade == 'C':
            return 3.0
        elif self.grade == 'D':
            return 2.0
        elif self.grade == 'E':
            return 1.0
        elif self.grade == 'F':
            return 0.0
        else:
            return None

