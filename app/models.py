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


class Book ( db.Model ):
    __tablename__ = "book"
    length = 8
    bookID = db.Column ( db.String ( 32 ), primary_key=True )
    category = db.Column ( db.String ( 32 ) )
    book_name = db.Column ( db.String ( 32 ) )
    press = db.Column ( db.String ( 32 ) )
    year = db.Column ( db.Numeric ( 4, 0 ) )
    author = db.Column ( db.String ( 32 ) )
    price = db.Column ( db.Numeric ( 10, 2 ) )
    amount = db.Column ( db.Integer )
    stock = db.Column ( db.Integer )

    def __init__(self, bookID, category, book_name, press, year, author, price, amount, stock):
        try:
            self.bookID = str ( bookID )
            self.category = str ( category )
            self.book_name = str ( book_name )
            self.press = str ( press )
            assert int ( year ) > 0 and int ( year ) < 10000, 'year not in (0,10000)'
            self.year = int ( year )
            self.author = str ( author )
            assert float ( price ) >= 0, 'Price should be non negative number'
            self.price = float ( price )
            assert int ( amount ) >= 0, 'Amount should be non negative integer'
            self.amount = int ( amount )
            assert int ( stock ) >= 0, 'Stock should be non negative integer'
            self.stock = int ( stock )
        except Exception as e:
            print ( e )
            raise e

    def __repr__(self):
        return '<Book Name %r>' % self.book_name
