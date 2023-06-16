

# Program Name

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

This program is designed to provide a web-based application for managing courses and calculating GPA and CGPA for students. It allows users to sign up, log in, add courses, edit courses, and view their GPA and CGPA based on the entered course grades and units. The program utilizes Flask, SQLAlchemy, and MongoDB for backend functionality and provides a user-friendly interface using HTML templates and forms.



## Table of Contents

- [Features](#features)

- [Installation](#installation)

- [Usage](#usage)

- [Testing](#testing)

- [API Documentation](#api-documentation)

- [Contributing](#contributing)

- [License](#license)

- [Google Slide Presentation](#google-slide-presentation)

- [Landing Page](#landing-page)

## Features

- User registration and authentication

- Course management (add, edit, delete)

- Calculation of GPA and CGPA

- Session management for logged-in users

- Error handling and flash messages

- Responsive and intuitive user interface

## Installation

1. Clone the repository:

   ```bash

   git clone https://github.com/your-username/your-repository.git

   ```

2. Install the required dependencies:

   ```bash

   pip install -r requirements.txt

   ```

3. Set up the database:

   

   - Modify the `config.py` file to configure the MongoDB connection settings.

   - Create a MongoDB database and collection for the application.

4. Set the environment variables:

   - Set the `FLASK_APP` environment variable to `app.py`.

   - Set the `SECRET_KEY` environment variable to a secure secret key.

5. Run the application:

   ```bash

   flask run

   ```

6. Open the web browser and navigate to `http://localhost:5000` to access the application.

## Usage

- Sign up as a new user or log in with your existing credentials.

- Add courses by providing the course details (code, title, unit, grade) and submit the form.

- View and manage your courses on the dashboard page.

- Edit or delete a course by selecting the respective options.

- Calculate your GPA and CGPA by clicking on the corresponding buttons.

## Testing

The program includes a comprehensive set of unit tests to ensure the functionality is working as expected. To run the tests, follow these steps:

1. Make sure you have installed the required dependencies as mentioned in the installation steps.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command:

   ```bash

   python -m unittest discover tests

   ```

   This command will automatically discover and run all the tests in the `tests` directory.

4. The test results will be displayed in the terminal, indicating the number of tests run and any failures or errors encountered.

## API Documentation

The program provides a set of API endpoints for interacting with the application's functionality programmatically. The API endpoints are designed following RESTful principles and return data in JSON format. The detailed API documentation can be found in the [API Documentation](api_documentation.md) file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or create an issue in the repository. Make sure to follow the existing code style and include relevant tests.

## License

This program is licensed under the MIT License. See the [

LICENSE](LICENSE) file for more information.

## Google Slide Presentation

Please refer to the [Google Slide Presentation](https://docs.google.com/presentation/d/1yVzFVcOVpRW-5QsjV1evuQMzs2ZpQFp4lkExLTL_MoA/edit?usp=drivesdk) for a detailed overview of the program, including its features, architecture, and usage.

## Landing Page

For more information about the developer and other projects, visit the [Portfolio Landing Page](http://Isybliss.github.io/portfolio-landing-page).

## Contact

For any inquiries or questions, please contact [Abakpa Dominic](mailto:abakpad82@gmail.com).
[Umunna Isioma](mailto:isyblissumunna@gmail.com)

