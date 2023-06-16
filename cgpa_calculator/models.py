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

        self.email = email

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

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, course_code, course_title, course_unit, grade, user_id):

        self.course_code = course_code

        self.course_title = course_title

        self.course_unit = course_unit

        self.grade = grade

        self.user_id = user_id

    def calculate_grade_point(self):

        """

        Calculates the Grade Point of the course's grade.

        """

        if self.grade == 'A':

            return 5.00

        elif self.grade == 'B':

            return 4.00

        elif self.grade == 'C':

            return 3.00

        elif self.grade == 'D':

            return 2.00

        elif self.grade == 'E':

            return 1.00

        else:

            return 0.00

    @staticmethod

    def calculate_gpa(course_units, grades):

        """

        Calculate the GPA given the course units and grades.

        """

        if not all(0.00 <= i <= 5.00 for i in grades):

            return {'error': 'Invalid grade value'}

        total_cu = sum(course_units)

        weighted_points = 0

        for i in range(len(course_units)):

            weighted_points += course_units[i] * grades[i]

        gpa = weighted_points / total_cu

        return round(gpa, 2)

    @staticmethod

    def calculate_cgpa_utme(level, sem, prev_cgpa, gpa):

        """

        Calculate the CGPA for UTME admission mode.

        """

        cgpa = prev_cgpa  # Initialize current CGPA to previous CGPA

        if level == 100:

            if sem == 1:

                cgpa = 0

            elif sem == 2:

                cgpa = (prev_cgpa + gpa) / 2

        elif level == 200:

            if sem == 1:

                cgpa = (prev_cgpa * 2 + gpa) / 3

            elif sem == 2:

                cgpa = (prev_cgpa * 3 + gpa) / 4

        elif level == 300:

            if sem == 1:

                cgpa = (prev_cgpa * 4 + gpa) / 5

            elif sem == 2:

                cgpa = (prev_cgpa * 5 + gpa) / 6

        elif level == 400:

            if sem == 1:

                cgpa = (prev_cgpa * 6 + gpa) / 7

            elif sem == 2:

                cgpa = (prev_cgpa * 7 + gpa) / 8

        elif level == 500:

            if sem == 1:

                cgpa = (prev_cgpa * 8 + gpa) / 9

            elif sem == 2:

                cgpa = (prev_cgpa * 9 + gpa) / 10

        elif level == 600:

            if sem == 1:

                cgpa = (prev_cgpa * 10 + gpa) / 11

            elif sem == 2:

                cgpa = (prev_cgpa * 11 + gpa) / 12

        return round(cgpa, 2)

    @staticmethod

    def calculate_cgpa_de(level, sem, prev_cgpa, gpa):

        """

        Calculate the CGPA for Direct Entry (DE) admission mode.

        """

        cgpa = prev_cgpa  # Initialize current CGPA to previous CGPA

        if level == 200:

            if sem == 1:

                cgpa = 0

            elif sem == 2:

                cgpa = (prev_cgpa + gpa) / 2

        elif level == 300:

            if sem == 1:

                cgpa = (prev_cgpa * 2 + gpa) / 3

            elif sem == 2:

                cgpa = (prev_cgpa * 3 + gpa) / 4

        elif level == 400:

            if sem == 1:

                cgpa = (prev_cgpa * 4 + gpa) / 5

            elif sem == 2:

                cgpa = (prev_cgpa * 5 + gpa) / 6

        elif level == 500:

            if sem == 1:

                cgpa = (prev_cgpa * 6 + gpa) / 7

            elif sem == 2:

                cgpa = (prev_cgpa * 7 + gpa) / 8

        elif level == 600:

            if sem == 1:

                cgpa = (prev_cgpa * 8 + gpa) / 9

            elif sem == 2:

                cgpa = (prev_cgpa * 9 + gpa) / 10

        return round(cgpa, 2)

