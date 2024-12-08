from flask import Blueprint, render_template,redirect, request, redirect, url_for, flash, session, current_app
from .models import Event, Participant
from .forms import EventForm, ParticipantForm, AdminLoginForm
from .extensions import mail
from flask_mail import Message
from .extensions import mail
bp = Blueprint('main', __name__)

# Route to display all events
@bp.route('/')
def home():
    events = Event.select()
    return render_template('home.html', events=events)

# Route to create a new event
@bp.route('/event/new', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event.create(
            name=form.name.data,
            description=form.description.data,
            date=form.date.data,
            location=form.location.data
        )
        flash('Event created successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_event.html', form=form)

# Route to register a participant for an event
@bp.route('/event/<int:event_id>/register', methods=['GET', 'POST'])
def register_participant(event_id):
    form = ParticipantForm()
    event = Event.get_or_none(Event.id == event_id)
    if form.validate_on_submit():
        participant = Participant.create(
            name=form.name.data,
            email=form.email.data,
            event=event
        )
        
        # Send a confirmation email to the participant
        msg = Message('Event Registration Confirmation', recipients=[form.email.data])
        msg.body = f'You have been successfully registered for {event.name}!'
        mail.send(msg)
        
        flash('Registration successful! A confirmation email has been sent.', 'success')
        return redirect(url_for('main.home'))
    return render_template('register_participant.html', form=form, event=event)

# Route: Admin Login
@bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if session.get('admin_logged_in'):
        return redirect(url_for('main.admin_dashboard'))

    form = AdminLoginForm()
    if form.validate_on_submit():
        admin_username = current_app.config['ADMIN_USERNAME']  # Access via current_app
        admin_password = current_app.config['ADMIN_PASSWORD']  # Access via current_app

        if form.username.data == admin_username and form.password.data == admin_password:
            session['admin_logged_in'] = True
            flash('Welcome, Admin!', 'success')
            return redirect(url_for('main.admin_dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('admin_login.html', form=form)
@bp.route('/admin/logout')
def admin_logout():
    """Logs the admin out and clears the session."""
    session.pop('admin_logged_in', None)  # Remove the admin login flag from the session
    flash('You have been logged out.', 'info')  # Optional: Show a logout message
    return redirect(url_for('main.admin_login'))  # Redirect to the login page

# Route: Admin Dashboard
@bp.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        flash('Please log in to access the admin dashboard.', 'warning')
        return redirect(url_for('main.admin_login'))

    events = Event.select()
    return render_template('admin_dashboard.html', events=events)

# Route: View Participants
@bp.route('/admin/event/<int:event_id>/participants')
def view_participants(event_id):
    if not session.get('admin_logged_in'):
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('main.admin_login'))

    event = Event.get_or_none(Event.id == event_id)
    participants = Participant.select().where(Participant.event == event)
    return render_template('view_participants.html', event=event, participants=participants)

# Route: Send Reminder Emails
@bp.route('/admin/event/<int:event_id>/send_reminders')
def send_reminders(event_id):
    if not session.get('admin_logged_in'):
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('main.admin_login'))

    event = Event.get_or_none(Event.id == event_id)
    participants = Participant.select().where(Participant.event == event)

    for participant in participants:
        msg = Message(
            subject=f"Reminder for {event.name}",
            recipients=[participant.email],
            body=f"Hi {participant.name},\n\nThis is a reminder for the event '{event.name}' happening on {event.date}.\n\nThanks!"
        )
        mail.send(msg)

    flash('Reminders sent to all participants!', 'success')
    return redirect(url_for('main.view_participants', event_id=event_id))
  