import os.path

import data as data
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
# from db import Book
from flask_bootstrap import Bootstrap
# from created_app import create_app
from flask_wtf import FlaskForm
from jinja2.nodes import Test
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length



#
# def create_app():
app = Flask(__name__)
with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = 'i love it'
    Bootstrap(app)
    db = SQLAlchemy(app)

    # db.create_all()

    # db.init_app(app)

app.app_context().push()



#CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

db.drop_all() # BIG Chance for solution....
db.create_all()

# new_book = Book(title=f'Harry Potter', author=f'J. K. Rowling', rating=9.6)
# db.session.add(new_book)
# db.session.commit()
#
# print(new_book.title)

class LibraryForm(FlaskForm):
    name = StringField(label='Book Name', validators=[DataRequired(), Length(min=6, max=200)])
    author = StringField(label='Book Author', validators=[DataRequired()])
    rating = StringField(label='Rating', validators=[DataRequired()])

    submit = SubmitField(label='submit')



all_books = []


@app.route('/')
def home():

    # if os.path.isfile('new-books-collection.db'):
        all_books = db.session.query(Book).all()

        print(all_books)
    # length_of_book = len(all_books)

        return render_template('index.html', books=all_books)#length_book=length_of_book


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = LibraryForm()


    if form.validate_on_submit():
        print('True')


        new_book = Book(title=f'{form.name.data}', author=f'{form.author.data}', rating=form.rating.data)
        db.session.add(new_book)
        db.session.commit()

        all_books = db.session.query(Book).all()

        print(all_books)


        return redirect('/')#, books=new_book, length_book=length_of_book , books=all_books

    return render_template('add.html', form=form)


@app.route('/edit/<book_id>', methods=['GET', 'POST'])# {{url_for('edit({{item['id']}})')}}
def edit(book_id):
    form = LibraryForm()

    if form.validate_on_submit():
        print('True')
        book_to_update = Book.query.get(book_id)
        print(book_to_update.title)
        book_to_update.title = form.name.data
        book_to_update.author = form.author.data
        book_to_update.rating = form.rating.data
        db.session.commit()

        all_books = db.session.query(Book).all()

        return render_template('index.html', books=all_books)# , books=all_books

    return render_template('edit.html', form=form)



@app.route('/<book_id>')
def delete(book_id):

    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect('/')



if __name__ == "__main__":

    app.run(debug=True)

