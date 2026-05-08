from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Movie Table
class Movie(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    movie = db.Column(db.String(200), nullable=False)

    director = db.Column(db.String(200), nullable=False)

    year = db.Column(db.Integer, nullable=False)

    genre = db.Column(db.String(100), nullable=False)

    poster = db.Column(db.String(500), nullable=False)

    favorite = db.Column(db.String(10), default="No")


# Create Database
with app.app_context():
    db.create_all()


# Home Page
@app.route("/")
def index():

    movies = Movie.query.order_by(Movie.year.desc()).all()

    return render_template("index.html", movies=movies)


# Add Movie
@app.route("/add", methods=["POST"])
def add_movie():

    movie = request.form["movie"]
    director = request.form["director"]
    year = request.form["year"]
    genre = request.form["genre"]
    poster = request.form["poster"]

    new_movie = Movie(
        movie=movie,
        director=director,
        year=year,
        genre=genre,
        poster=poster,
        favorite="No"
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect("/")


# Favorite Toggle
@app.route("/favorite/<int:id>")
def favorite(id):

    movie = Movie.query.get_or_404(id)

    if movie.favorite == "Yes":
        movie.favorite = "No"
    else:
        movie.favorite = "Yes"

    db.session.commit()

    return redirect("/")


# Delete Movie
@app.route("/delete/<int:id>")
def delete_movie(id):

    movie = Movie.query.get_or_404(id)

    db.session.delete(movie)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)