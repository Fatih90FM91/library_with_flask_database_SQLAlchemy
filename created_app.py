from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'i love it'
    Bootstrap(app)


    return app




# app = create_app()
# with app.app_context():
#     db = SQLAlchemy(app)
#     app = create_app()
#     app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#     # Optional: But it will silence the deprecation warning in the console.
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.init_app(app)
#
#     db.create_all()
# app.app_context().push()

# app = create_app()
# # app.app_context().push()
# db = SQLAlchemy(app)
# #
# #
# #