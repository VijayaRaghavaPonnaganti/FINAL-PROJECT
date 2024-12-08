from flask import Flask, g
import os
from peewee import SqliteDatabase
from .models import db, Event, Participant
from flask_mail import Mail, Message
from .forms import EventForm, ParticipantForm
from .routes import bp
from .extensions import mail

mail = Mail()

def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))
    
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'vijayaraghava.ponnaganti@gmail.com'
    app.config['MAIL_DEFAULT_SENDER'] = 'vijayaraghava.ponnaganti@gmail.com'
    app.config['MAIL_PASSWORD'] = 'tsda thce hzcn aehd'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['ADMIN_USERNAME'] = 'admin'
    app.config['ADMIN_PASSWORD'] = 'password'  # Use a secure password in production
    app.config['SECRET_KEY'] = 'your_secure_secret_key'

    
    mail.init_app(app)
    
    app.register_blueprint(bp)
    
    # Database connection management
    @app.before_request
    def before_request():
        """Connect to the database before each request."""
        if not hasattr(g, 'db'):
            g.db = db
            g.db.connect()
        
        # Create tables if they do not exist
        db.create_tables([Event, Participant], safe=True)

    @app.teardown_request
    def teardown_request(exception=None):
        """Close the database connection after each request."""
        db_connection = getattr(g, 'db', None)
        if db_connection is not None:
            db_connection.close()


    return app
