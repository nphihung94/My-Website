# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Data(db.Model):
    
    """ Create the database for website: projects(name, programming language, description)
    Create data and allow users to interact with data include: create table, 
    insert, delete or modify an instance, look up for data."""
    
    # Create table Projects_List(name, programming_language, description, git_url)
    __tablename__ = "Projects_List"
    id = db.Column(db.Integer, unique = True, primary_key = True)
    name = db.Column(db.String, unique = True)
    programming_language = db.Column(db.String)
    description = db.Column(db.String)
    git_url = db.Column(db.String)
    def __init__(self, name, programming_language,description,git_url):
        self.name = name
        self.programming_language = programming_language
        self.description = description
        self.git_url = git_url

    def __repr__(self):
        return "<Project(id='%d',name='%s', programming_language='%s', description='%s', git_url='%s')>" % (
                self.id,self.name, self.programming_language, self.description, self.git_url)