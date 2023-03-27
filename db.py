from created_app import create_app
from flask_sqlalchemy import SQLAlchemy







##CREATE DATABASE
# db = SQLAlchemy() # db intitialized here
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://test.db"
# db.init_app(app)
app = create_app()
with app.app_context():
    db = SQLAlchemy()
    # app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
    # Optional: But it will silence the deprecation warning in the console.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    db.create_all()


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# db.create_all()





