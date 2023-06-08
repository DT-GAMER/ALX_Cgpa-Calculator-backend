from flask import Flask, render_template, request, redirect, url_for, flash, session

from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm, SignUpForm, AddCourseForm, EditCourseForm

from models import User, Course

from utils import calculate_gpa, calculate_cgpa_utme, calculate_cgpa_de

app = Flask(__name__)

app.config.from_object('config')

# Initialize the PostgreSQL database connection

db = SQLAlchemy(app)

# Set a secret key for session management

app.secret_key = 'your-secret-key-goes-here'

@app.route('/signup', methods=['GET', 'POST'])

def signup():

    form = SignUpForm()

    if form.validate_on_submit():

        user = User(

            first_name=form.first_name.data,

            last_name=form.last_name.data,

            email=form.email_address.data,

            password=form.password.data

        )

        db.session.add(user)

        db.session.commit()

        flash('Signup successful!', 'success')

        return redirect(url_for('login'))

    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])

def login():

    form = LoginForm()

    if form.validate_on_submit():

        email = form.email_address.data

        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):

            # Store user ID in session

            session['user_id'] = user.id

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

    user = User.query.get(session['user_id'])

    courses = Course.query.filter_by(user_id=user.id).all()

    return render_template('dashboard.html', user=user, courses=courses)

@app.route('/course/add', methods=['GET', 'POST'])

def add_course():

    form = AddCourseForm()

    if form.validate_on_submit():

        course = Course(

            course_code=form.course_code.data,

            course_title=form.course_title.data,

            course_unit=form.course_unit.data,

            grade=form.grade.data,

            user_id=session['user_id']  # Associate the course with the current user

        )

        db.session.add(course)

        db.session.commit()

        flash('Course added successfully!', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_course.html', form=form)

@app.route('/course/edit/<int:course_id>', methods=['GET', 'POST'])

def edit_course(course_id):

    course = Course.query.get(course_id)

    if not course:

        flash('Course not found.', 'error')

        return redirect(url_for('dashboard'))

    form = EditCourseForm(obj=course)

    if form.validate_on_submit():

        form.populate_obj(course)

        db.session.commit()

        flash('Course updated successfully!', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_course.html', form=form)

@app.route('/course/delete/<int:course_id>', methods=['POST'])

def delete_course(course_id):

    course = Course.query.get(course_id)

    if not course:

        flash('Course not found.', 'error')

        return redirect(url_for('dashboard'))

    db.session.delete(course)

    db.session.commit()

    flash('Course deleted successfully!', 'success')

    return redirect(url_for('dashboard'))

@app.route('/calculate', methods=['POST'])

def generate_result():

    if 'user_id' not in session:

        flash('Please log in to calculate the result.', 'error')

        return redirect(url_for('login'))

    # Rest of the code for calculating the result goes here

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

