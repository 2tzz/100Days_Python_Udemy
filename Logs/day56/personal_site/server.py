from flask import Flask , render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") 



if __name__ == "__main__" :
    #run in debug mode to auto run server whenever makes a change
    app.run(debug=True) 
   

