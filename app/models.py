from app import db


# BaseModel = declarative_base ()


class Admin ( db.Model ):
    __tablename__ = "admin"
    id = db.Column ( db.Integer, primary_key=True )
    password = db.Column ( db.String ( 32 ) )
    name = db.Column ( db.String ( 32 ), index=True )
    contact = db.Column ( db.String ( 32 ), index=True )

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __init__(self, id, password, name, contact):
        self.id = id
        self.password = password
        self.name = name
        self.contact = contact

    # For debug
    def __repr__(self):
        return '<User %r>' % self.name
