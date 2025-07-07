from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get data from form
        username = request.form['username']
        password = request.form['password']
        
        
    
    # GET method just renders the form
    return render_template("success.html", username=username, password=password)


if __name__ == "__main__":
    app.run(debug=True)
