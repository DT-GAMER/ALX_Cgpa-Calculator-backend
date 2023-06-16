import unittest

from app import app, mongo

class AppTestCase(unittest.TestCase):

    @classmethod

    def setUpClass(cls):

        # Set up any necessary test data before running the tests

        with app.app_context():

            # Create test users

            user1 = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'password': 'password1'}

            user2 = {'first_name': 'Jane', 'last_name': 'Smith', 'email': 'jane@example.com', 'password': 'password2'}

            mongo.db.users.insert_many([user1, user2])

    @classmethod

    def tearDownClass(cls):

        # Clean up any resources after running the tests

        with app.app_context():

            # Remove test users

            mongo.db.users.delete_many({})

    def setUp(self):

        # Set up any necessary test data before each test method

        self.client = app.test_client()

    def tearDown(self):

        # Clean up any resources after each test method

        pass

    def test_signup_success(self):

        # Test successful user signup

        response = self.client.post('/signup', data={

            'first_name': 'Test',

            'last_name': 'User',

            'email': 'test@example.com',

            'password': 'password123'

        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Signup successful!', response.data)

    def test_signup_existing_email(self):

        # Test signup with an existing email address

        response = self.client.post('/signup', data={

            'first_name': 'Test',

            'last_name': 'User',

            'email': 'john@example.com',  # Existing email

            'password': 'password123'

        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'This email is already taken.', response.data)

    def test_login_success(self):

        # Test successful user login

        response = self.client.post('/login', data={

            'email': 'john@example.com',

            'password': 'password1'

        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Login successful!', response.data)

    def test_login_invalid_credentials(self):

        # Test login with invalid credentials

        response = self.client.post('/login', data={

            'email': 'john@example.com',

            'password': 'incorrect-password'

        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Invalid email or password.', response.data)

      def test_add_course(self):

        # Test adding a course

        with app.app_context():

            # Create a test user

            user = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'password': 'password'}

            mongo.db.users.insert_one(user)

            user_id = str(user['_id'])

        # Log in as the test user

        self.client.post('/login', data={'email': 'john@example.com', 'password': 'password'}, follow_redirects=True)

        # Add a course

        response = self.client.post('/course/add', data={

            'code': 'CS101',

            'title': 'Introduction to Computer Science',

            'unit': 3,

            'grade': 'A'

        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Course added successfully!', response.data)

        # Check if the course is added to the user's dashboard

        with app.app_context():

            courses = mongo.db.courses.find({'user_id': user_id})

            self.assertEqual(courses.count(), 1)

            self.assertEqual(courses[0]['code'], 'CS101')

    def test_edit_course(self):

        # Test editing a course

        with app.app_context():

            # Create a test user

            user = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'password': 'password'}

            mongo.db.users.insert_one(user)

            user_id = str(user['_id'])

            # Create a test course

            course = {'code': 'CS101', 'title': 'Introduction to Computer Science', 'unit': 3, 'grade': 'A', 'user_id': user_id}

            mongo.db.courses.insert_one(course)

            course_id = str(course['_id'])

        # Log in as the test user

        self.client.post('/login', data={'email': 'john@example.com', 'password': 'password'}, follow_redirects=True)

        # Edit the course

        response = self.client.post(f'/course/edit/{course_id}', data={

            'code': 'CS102',

            'title': 'Advanced Computer Science',

            'unit': 4,

            'grade': 'B'

        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Course updated successfully!', response.data)

        # Check if the course is updated in the database

        with app.app_context():

            updated_course = mongo.db.courses.find_one({'_id': course_id})

            self.assertEqual(updated_course['code'], 'CS102')

            self.assertEqual(updated_course['title'], 'Advanced Computer Science')

            self.assertEqual(updated_course['unit'], 4)

            self.assertEqual(updated_course['grade'], 'B')

    def test_delete_course(self):

        # Test deleting a course

        with app.app_context():

            # Create a test user

            user = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'password': 'password'}

            mongo.db.users.insert_one(user)

            user_id = str(user['_id'])

            # Create a test course

            course = {'code': 'CS101', 'title': 'Introduction to Computer Science', 'unit': 3, 'grade': 'A', 'user_id': user_id}

            mongo.db.courses.insert_one(course)

            course_id = str(course['_id'])

        # Log in as the test user

        self.client.post('/login', data={'email': 'john@example.com', 'password': 'password'}, follow_redirects=True)

        # Delete the course

        response = self.client.post(f'/course/delete/{course_id}', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Course deleted successfully!', response.data)

        # Check if the course is deleted from the database

        with app.app_context():

            deleted_course = mongo.db.courses.find_one({'_id': course_id})

            self.assertIsNone(deleted_course)

if __name__ == '__main__':

    unittest.main()

