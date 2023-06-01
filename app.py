from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, SignUpForm, AddCourseForm, EditCourseForm
from models import User, Course
from utils import calculate_gpa, calculate_cgpa_utme, calculate_cgpa_de

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route('/signup', methods=['POST'])
def signup():
    form = SignUpForm(request.json)
    
    if form.validate():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email_address.data,
            password=form.password.data<F11>
        )
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({'message': 'Signup successful'})
    
    return jsonify({'errors': form.errors}), 400


@app.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.json)
    
    if form.validate():
        email = form.email_address.data
        password = form.password.data
        
        user = User.query.filter_by(email=email_address).first()
        
        if user and user.check_password(password):
            return jsonify({'message': 'Login successful'})
        
        return jsonify({'error': 'Invalid email or password'}), 401
    
    return jsonify({'errors': form.errors}), 400


@app.route('/course/add', methods=['POST'])
def add_course():
    form = AddCourseForm(request.json)
    
    if form.validate():
        course = Course(
            code=form.code.data,
            title=form.title.data,
            unit=form.unit.data,
            grade=form.grade.data
        )
        
        db.session.add(course)
        db.session.commit()
        
        return jsonify({'message': 'Course added successfully'})
    
    return jsonify({'errors': form.errors}), 400


@app.route('/course/edit/<int:course_id>', methods=['PUT'])
def edit_course(course_id):
    form = EditCourseForm(request.json)
    
    if form.validate():
        course = Course.query.get(course_id)
        
        if not course:
            return jsonify({'error': 'Course not found'}), 404
        
        course.code = form.code.data
        course.title = form.title.data
        course.unit = form.unit.data
        course.grade = form.grade.data
        
        db.session.commit()
        
        return jsonify({'message': 'Course updated successfully'})
    
    return jsonify({'errors': form.errors}), 400


@app.route('/course/delete/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get(course_id)
    
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    
    db.session.delete(course)
    db.session.commit()
    
    return jsonify({'message': 'Course deleted successfully'})


@app.route('/calculate', methods=['POST'])
def generate_result():
    data = request.json
    
    admission_mode = data['admission_mode']
    course_units = data['course_units']
    grades = data['grades']
    level = data['level']
    sem = data['sem']
    prev_cgpa = data['prev_cgpa']
    
    gpa = calculate_gpa(course_units, grades)
    
    if admission_mode == 'UTME':
        cgpa = calculate_cgpa_utme(level, sem, prev_cgpa, gpa)
    elif admission_mode == 'DE':
        cgpa = calculate_cgpa_de(level, sem, prev_cgpa, gpa)
    else:
        return jsonify({'error': 'Invalid admission mode'})
    
    result = {
        'Course Units': course_units,
        'Grades': grades,
        'GPA': gpa,
        'CGPA': cgpa
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run()


