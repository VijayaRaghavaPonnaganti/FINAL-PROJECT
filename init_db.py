from app.models import db, Event, Participant

# Connect to the database
db.connect()

# Create the tables
db.create_tables([Event, Participant], safe=True)

print("Database initialized and tables created.")
