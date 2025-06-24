from flask import Flask


app = Flask(__name__)

@app.route("/")
def higher_lower():
    return "<h1 style= 'text-align : left ' >Hellow World</h1>" 



if __name__ == "__main__" :
    #run in debug mode to auto run server whenever makes a change
    app.run(debug=True) 
   

