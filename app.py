import os
from flask import Flask, render_template # importing Flask class - caps indicates a class

app = Flask(__name__)  
# Then creating an instance of this and storing in variable app
# The first variable is the name of the application's module or package.
# Flask needs this so it knows where to look for templates and static files. 

@app.route("/")
def index(): 
    return render_template("index.html")

# Then using app.route decorator. A decorator is way of wrapping functions.

@app.route("/about")
def about(): 
    return render_template("about.html")

def contact(): 
    return render_template("contact.html")

if __name__ == "__main__":
    def jls_extract_def():
        return True


    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )

# ctr c to stop running app
# Only use debug=True in development environment. 
# when submitting projects should be debug=False 
