from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


# class BookForm(FlaskForm):
#     cafe = StringField('Cafe name', validators=[DataRequired()])
#     location = StringField('location', validators=[DataRequired()])
    
all_books = [
    {
        "title": "Harry Potter",
        "author": "J. K. Rowling",
        "rating": 9,
    },
    
    {
        "title": "Tale of two cities",
        "author": "Charles Dickens",
        "rating": 7,
    }
    ]


@app.route('/')
def home():
    
    return render_template('index.html' , books = all_books )


@app.route("/add" , methods=['GET', 'POST'] )
def add():
    if request.method == 'POST':
        # Get data from form
        book_name = request.form['book']
        book_author = request.form['auth']
        book_rating = request.form['rating']
    return render_template('add.html' )


if __name__ == "__main__":
    app.run(debug=True)

