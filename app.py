import os
import json
from flask import Flask, render_template, request, flash 
if os.path.exists("env.py"): 
    import env # a __pycache__ file is created. Add to gitignore. the / at the end identifies it as a directory, so will ignore all in it too. 

# But, we only want to import env, if the system can find an env.py file.
# if os.path.exists("env.py"): import env
# Once we save that, a new directory called 'pycache' is created.
# We don't need to bother pushing that to GitHub either, so let's go back into our .gitignore
# file and type: __pycache__/.
# The '/' at the end identifies it sas a directory, and so will therefore ignore everything within
# that folder as well.

# importing Flask class - caps indicates a class, render_template and request
# import function called flash so can display flashed message to user when form submitted. 




# Letters next to files: 
# u untracked - if add to gitignore will disappear as not being tracked by github. 
# m modified since last committ. 

app = Flask(__name__)  
# Then creating an instance of this and storing in variable app
# The first variable is the name of the application's module or package.
# Flask needs this so it knows where to look for templates and static files. 

app.secret_key = os.environ.get("SECRET_KEY") #then going to call the flash() function from our contact form. 

@app.route("/")
def index(): 
    return render_template("index.html")

# Then using app.route decorator. A decorator is way of wrapping functions.

@app.route("/about")
def about(): 
    data = [] # initialise empty array - importing from json
    with open("data/company.json", "r") as json_data: # opening contents of file as read only "r" assigning contents to variable "json_data"
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data) 
    # Creating new variable company which is loading json_data with command json.load.

@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name: 
                member = obj
    return render_template("member.html", member=member)

@app.route("/careers")
def careers(): 
    return render_template("careers.html", page_title="Come Work with Us")


@app.route("/contact", methods=["GET", "POST"])
def contact(): 
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form.get("name")))

    return render_template("contact.html", page_title="Contact Us")

# I'm going to call the
# Flash() function.
# flash("Thanks {}, we have received your message!".format(request.form.get("name"))).

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
