#!/usr/bin/python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Adress', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email Adress', validators=[DataRequired(), Email()])
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
