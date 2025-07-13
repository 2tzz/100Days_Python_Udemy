from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired, URL, NumberRange
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY', '8BYkEfBA6O6donzWlSihBXox7C0sKR6b')
Bootstrap5(app)

# TMDB API Configuration
TMDB_API_KEY = os.environ.get('TMDB_API_KEY', '5a4c024c86878e1eac53e186f5c6d373')
TMDB_HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.environ.get('TMDB_ACCESS_TOKEN', 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YTRjMDI0Yzg2ODc4ZTFlYWM1M2UxODZmNWM2ZDM3MyIsIm5iZiI6MTc1MjMyNzE3Ni44MjcwMDAxLCJzdWIiOiI2ODcyNjQwODkxOTUxN2FjZTlhOTgwYjciLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.7z7aPFPHy_0egG6yaJfOa7_WBVkFi02Gdl4PSc_-Kiw')}"
}
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

# Database Setup
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)

# Forms
class SearchForm(FlaskForm):
    movie = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Search')

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rating = FloatField('Rating (1-10)', validators=[
        DataRequired(),
        NumberRange(min=0, max=10, message="Rating must be between 0 and 10")
    ])
    review = TextAreaField('Your Review', validators=[DataRequired()])
    img_url = StringField('Poster URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Submit')

# Models
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route("/")
def home():
    movies = Movie.query.order_by(desc(Movie.rating)).all()
    
    # Update rankings based on current ratings
    for i, movie in enumerate(movies, start=1):
        movie.ranking = i
    db.session.commit()
    
    return render_template("index.html", movies=movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        try:
            new_movie = Movie(
                title=form.title.data,
                year=form.year.data,
                description=form.description.data,
                rating=form.rating.data,
                review=form.review.data,
                img_url=form.img_url.data,
                ranking=None
            )
            db.session.add(new_movie)
            db.session.commit()
            flash('Movie added successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding movie: {str(e)}', 'danger')
    return render_template("add.html", form=form)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    movie = db.get_or_404(Movie, id)
    form = MovieForm(obj=movie)
    if form.validate_on_submit():
        try:
            form.populate_obj(movie)
            db.session.commit()
            flash('Movie updated successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating movie: {str(e)}', 'danger')
    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete/<int:id>")
def delete(id):
    movie = db.get_or_404(Movie, id)
    try:
        db.session.delete(movie)
        db.session.commit()
        flash('Movie deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting movie: {str(e)}', 'danger')
    return redirect(url_for('home'))

@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        try:
            movie_name = form.movie.data.strip().replace(' ', '+')
            url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}"
            response = requests.get(url, headers=TMDB_HEADERS)
            response.raise_for_status()
            data = response.json()
            
            if not data.get('results'):
                flash('No movies found with that title.', 'info')
                return redirect(url_for('search'))
                
            return render_template("search.html", results=data['results'], form=form)
        except requests.RequestException as e:
            flash(f'Error searching movies: {str(e)}', 'danger')
    return render_template("search.html", form=form)

@app.route("/add_from_api/<int:movie_id>")
def add_from_api(movie_id):
    try:
        # Get movie details
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        response = requests.get(url, headers=TMDB_HEADERS)
        response.raise_for_status()
        data = response.json()
        
        # Check if movie already exists
        if Movie.query.filter_by(title=data['title']).first():
            flash('This movie already exists in your collection!', 'warning')
            return redirect(url_for('home'))
        
        # Create new movie
        new_movie = Movie(
            title=data['title'],
            year=data['release_date'].split('-')[0] if data.get('release_date') else None,
            description=data.get('overview', 'No description available'),
            rating=round(data.get('vote_average', 0), 1),
            review='Added from TMDB',
            img_url=f"{TMDB_IMAGE_BASE_URL}{data['poster_path']}" if data.get('poster_path') else "",
            ranking=None
        )
        
        db.session.add(new_movie)
        db.session.commit()
        flash(f'{new_movie.title} added successfully!', 'success')
        return redirect(url_for('edit', id=new_movie.id))
        
    except requests.RequestException as e:
        flash(f'Error fetching movie details: {str(e)}', 'danger')
        return redirect(url_for('search'))
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding movie: {str(e)}', 'danger')
        return redirect(url_for('search'))

if __name__ == '__main__':
    app.run(debug=True)