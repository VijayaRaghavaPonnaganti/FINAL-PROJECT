->Project Overview
git link:https://github.com/VijayaRaghavaPonnaganti/FINAL-PROJECT.git


The Event Management System (EMS) is a web-based platform that simplifies event organization. It allows administrators to create events, manage participant registrations, and send notifications to attendees. The system is built using Flask for the backend, Peewee ORM for database operations, and Flask-Mail for automated email notifications.

Key Features:
- Admin Dashboard: Manage events and view participants.
- Participant Registration: User-friendly forms for event registration.
- Notifications: Automated email updates to participants.
- Scalable Architecture: Modular design using Flask Blueprints.



->Steps to Set Up and Run the Code


1. Set Up a Virtual Environment:
   - Create and activate a Python virtual environment:
     python -m venv venv
     source venv/bin/activate  # For Linux/Mac
     venv\Scripts\activate     # For Windows
     

2. Install Dependencies:
   - Install the required Python libraries:

     pip install flask peewee flask-mail email-validator
 

3. Configure SMTP for Emails:
   - Update the `config.py` file with your email server details for Flask-Mail:

     MAIL_SERVER = 'smtp.gmail.com'
     MAIL_PORT = 587
     MAIL_USE_TLS = True
     MAIL_USERNAME = 'your-email@gmail.com'
     MAIL_PASSWORD = 'your-app-password'
    

4. Set Up the Database:
   - Run the following Python script to initialize the SQLite database:
   
     from app.models import db
     db.connect()
     db.create_tables([Event, Participant])
     print("Database initialized!")
 
5. Run the Application:
   - Start the Flask development server:

     python run.py

   - Access the application in your browser at `http://127.0.0.1:5000`.

-> Dependencies and Prerequisites

Dependencies
1. Flask: Web framework for creating the application.
2. Peewee ORM: Simplifies database operations.
3. Flask-Mail: Handles email notifications.
4. Email-Validator: Validates participant email addresses.
5. Werkzeug: Provides security and utility functions.
6. SQLite: Lightweight database system for storing events and participants.

Prerequisites
 Python 3.8 or higher.
 An SMTP email server for notifications.
 Basic knowledge of Flask and relational databases.


Explanation of the Main Files

1. run.py
    The entry point of the application.
    Creates and runs the Flask app using configurations from the `app/` directory.
    Example:
     from app import create_app
     app = create_app()

     if __name__ == "__main__":
         app.run(debug=True)
    

2. app/__init__.py
   - Initializes the Flask app and registers Blueprints for routing.
   - Configures extensions like Flask-Mail and database connection.

3. app/models.py
   - Defines the database schema using Peewee ORM.
   - Contains models like `Event` and `Participant`.

   python
   class Event(Model):
       name = CharField()
       description = TextField()
       date = DateField()
       location = CharField()
  

4. `app/routes.py`
   - Defines application routes for handling requests.
   - Includes routes for:
     - Admin dashboard.
     - Event creation.
     - Participant registration.
     - Viewing participants.

5. `app/templates/`
   - Contains Jinja2 HTML templates for rendering pages dynamically.
   - Templates include:
     - `admin_dashboard.html`: Admin interface for managing events.
     - `register.html`: Registration form for participants.
     - `view_participants.html`: Displays participants for a specific event.

6. `app/static/`
   - Contains static assets like CSS files for styling the application.

7. `config.py`
   - Stores application configuration settings, such as secret keys and SMTP credentials.

8. `app/forms.py` (Optional, if using Flask-WTF)
   - Defines form structures for event creation and participant registration.
   - Example:
     ```python
     class RegistrationForm(FlaskForm):
         name = StringField('Name', validators=[DataRequired()])
         email = EmailField('Email', validators=[DataRequired(), Email()])
         submit = SubmitField('Register')

Summary
Project Overview: A tool for managing events efficiently.
Setup Steps: Detailed steps to install dependencies, configure the database, and run the application.
Dependencies and Prerequisites: Lists the tools and libraries required for smooth functioning.
Main Files Explanation: Provides a clear understanding of each file's role in the application.

Let me know if you need more details on any section!