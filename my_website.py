# -*- coding: utf-8 -*-
from flask import Flask, render_template,request
from config import Config
from database import db,Data

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the tables of data needed
def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()

# execute query to get list of all rows in database
def get_all_data():
    return db.session.query(Data).all()

# return homepage
@app.route('/')
def home():
    return render_template("home.html")

# return page with list of project
@app.route('/project/')
def project():
    project_list = get_all_data()
    return render_template("projects.html",project_list = project_list)

# return page with button to move to add or modify/delete data 
# hidden page 
@app.route('/data/')
def data():
    return render_template("Data.html")

# return page allow adding new data to database
@app.route('/add/')
def add():
    return render_template("add.html")

# return page allow modify an instance in database
@app.route('/modify/')
def modify():
    project_list = get_all_data()
    if len(project_list) != 0:
        return render_template("modify.html",project_list = project_list)
    else:
        return render_template("Empty_database.html")

# return page allow delete an instance in database
@app.route('/delete/')
def delete():
    project_list = get_all_data()
    if len(project_list) != 0:
        return render_template("delete.html",project_list = project_list)
    else:
        return render_template("Empty_database.html")


# return success after finish editing database
@app.route('/success/',methods=['POST'])
def success():
    
    if request.method == 'POST':
        action = request.form["action"]
        # Adding a new data into database
        if action == "add":
            name = request.form["Project_name"]
            programming_language = request.form["Programming_Language"]
            description = request.form["description"]
            git_url = request.form["git_url"]
            request_data = Data(name,programming_language,description,git_url)
            db.session.add(request_data)
            db.session.commit()
            return render_template("success.html")
        
        # Modify already exist database
        elif action == "modify":
            id = request.form["id"]
            name = request.form["Project_name"]
            programming_language = request.form["Programming_Language"]
            description = request.form["description"]
            git_url = request.form["git_url"]
            modify_object = Data.query.filter_by(id=id).one()
            if len(name) != 0:
                modify_object.name = name
            if len(programming_language) != 0:
                modify_object.programming_language = programming_language
            if len(description) != 0:
                modify_object.description = description
            if len(git_url) != 0:
                modify_object.git_url = git_url
            db.session.commit()
            return render_template("success.html")
        
        # Delete an instance from data
        elif action == "delete":
            id = request.form["id"]
            delete_object = Data.query.filter_by(id=id).one()
            db.session.delete(delete_object)
            db.session.commit()
            return render_template("success.html")
   
if __name__ == "__main__":
    init_db()
    app.run(port = 1994,debug=True)