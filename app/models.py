from peewee import *

# Initialize the database
db = SqliteDatabase('events.db')

class BaseModel(Model):
    class Meta:
        database = db

# Event model
class Event(BaseModel):
    name = CharField()
    description = TextField()
    date = DateField()
    location = CharField()

# Participant model
class Participant(BaseModel):
    name = CharField()
    email = CharField()
    event = ForeignKeyField(Event, backref='participants')
    registered_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

# Initialize the database tables
db.connect()
db.create_tables([Event, Participant], safe=True)
