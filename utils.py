from typing import List

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, Email, Length, EqualTo

class SignUpForm(FlaskForm):

    first_name = StringField('First Name', validators=[DataRequired()])

    last_name = StringField('Last Name', validators=[DataRequired()])

    email = StringField('Email Address', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):

    email = StringField('Email Address', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Log In')

class AddCourseForm(FlaskForm):

    course_code = StringField('Course Code', validators=[DataRequired()])

    course_title = StringField('Course Title', validators=[DataRequired()])

    course_unit = StringField('Course Unit', validators=[DataRequired()])

    grade = StringField('Grade', validators=[DataRequired()])

    submit = SubmitField('Add Course')

class EditCourseForm(FlaskForm):

    course_code = StringField('Course Code', validators=[DataRequired()])

    course_title = StringField('Course Title', validators=[DataRequired()])

    course_unit = StringField('Course Unit', validators=[DataRequired()])

    grade = StringField('Grade', validators=[DataRequired()])

    submit = SubmitField('Save Changes')

    delete = SubmitField('Delete Course')

def calculate_grade_point(grade: str) -> float:

    """

    Calculates the Grade Point of a given grade.

    """

    if grade == 'A':

        return 5.00

    elif grade == 'B':

        return 4.00

    elif grade == 'C':

        return 3.00

    elif grade == 'D':

        return 2.00

    elif grade == 'E':

        return 1.00

    else:

        return 0.00

def calculate_gpa(course_units: List[float], grades: List[str]) -> float:

    """

    Calculate the GPA given the course units and grades.

    """

    if not all(0.00 <= i <= 5.00 for i in course_units):

        return {'error': 'Invalid course unit value'}

    

    total_cu = sum(course_units)

    weighted_points = 0

    

    for i in range(len(course_units)):

        weighted_points += course_units[i] * calculate_grade_point(grades[i])

    

    gpa = weighted_points / total_cu

    return round(gpa, 2)

def calculate_cgpa_utme(level: int, sem: int, prev_cgpa: float, gpa: float) -> float:

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

def calculate_cgpa_de(level: int, sem: int, prev_cgpa: float, gpa: float) -> float:

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

def generate_result(data: dict) -> dict:

    """

    Generates and returns the result given the data.

    """

    admission_mode = data['admission_mode']

    course_codes = data['course_codes']

    course_units = data['course_units']

    grades = data['grades']

    level = data['level']

    sem = data['sem']

    prev_cgpa = data['prev_cgpa']

    gpa = calculate_gpa(course_units, grades)

    cgpa = calculate_cgpa_utme(level, sem, prev_cgpa, gpa)

    result = {

        'admission_mode': admission_mode,

        'course_codes': course_codes,

        'course_units': course_units,

        'grades': grades,

        'gpa': gpa,

        'cgpa': cgpa

    }

    return result

def validate_input_data(data: dict) -> bool:

    """

    Validates the input data to ensure all required fields are present.

    """

    required_fields = ['admission_mode', 'course_codes', 'course_units', 'grades', 'level', 'sem', 'prev_cgpa']

    for field in required_fields:

        if field not in data:

            return False

    return True

