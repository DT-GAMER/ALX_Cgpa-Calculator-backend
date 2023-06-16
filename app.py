from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_pymongo import PyMongo
from flask_cors import CORS
from forms import LoginForm, SignUpForm, AddCourseForm, EditCourseForm
from models import User, Course
from utils import calculate_gpa, calculate_cgpa_utme, calculate_cgpa_de
import os

app = Flask(__name__)
app.config.from_object('config.Config')

mongo = PyMongo(app)

# Set a secret key for session management
app.secret_key = 'SECRET_KEY'


@app.route('/signup', methods=['GET', 'POST'] )
def signup():
    form = SignUpForm()
    
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data
        )
        
        mongo.db.users.insert_one(user.to_dict())
        
        flash('Signup successful!', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = mongo.db.users.find_one({'email': email})
        
        if user and User.validate_password(user['password'], password):
            # Store user ID in session
            session['user_id'] = str(user['_id'])
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        
        flash('Invalid email or password.', 'error')
    
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    # Clear the session and redirect to the login page
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))
    
    user = mongo.db.users.find_one({'_id': session['user_id']})
    courses = mongo.db.courses.find({'user_id': session['user_id']})
    
    return render_template('dashboard.html', user=user, courses=courses)


@app.route('/course/add', methods=['GET', 'POST'])
def add_course():
    form = AddCourseForm()
    
    if form.validate_on_submit():
        course = Course()
            code=form.code.data,
            title=form.title.data,
            unit=form.unit.data,
            grade=form.grade.data,
            user_id=session['user_id']  # Associate the course with the current user
        )
        
        mongo.db.courses.insert_one(course.to_dict())
        
        flash('Course added successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('add_course.html', form=form)


@app.route('/course/edit/<string:course_id>', methods=['GET', 'POST'])
def edit_course(course_id):
    course = mongo.db.courses.find_one({'_id': course_id})
    
    if not course:
        flash('Course not found.', 'error')
        return redirect(url_for('dashboard'))
    
    form = EditCourseForm(obj=course)
    
    if form.validate_on_submit():
        form.populate_obj(course)
        
        mongo.db.courses.update_one({'_id': course_id}, {'$set': course})
        
        flash('Course updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('edit_course.html', form=form)


@app.route('/course/delete/<string:course_id>', methods=['POST'])
def delete_course(course_id):
    course = mongo.db.courses.find_one({'_id': course_id})
    
    if not course:
        flash('Course not found.', 'error')
        return redirect(url_for('dashboard'))
    
    mongo.db.courses.delete_one({'_id': course_id})
    
    flash('Course deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

<F11>
@app.route('/calculate', methods=['POST'])
def generate_result():
    if 'user_id' not in session:
        flash('Please log in to calculate the result.', 'error')
        return redirect(url_for('login'))

@app.route('/')
def application_great():
    return 'This application is great!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

