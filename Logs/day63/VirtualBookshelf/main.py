from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    rating: Mapped[float]

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)



    


@app.route('/')
def home():
    books = db.session.execute(db.select(User)).scalars().all()
    return render_template('index.html', books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = User(
            title=request.form['title'],
            author=request.form['author'],
            rating=float(request.form['rating'])
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update():
    book = db.get_or_404(User, id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.rating = float(request.form['rating'])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('index.html', book=book)



if __name__ == "__main__":
    app.run(debug=True)

