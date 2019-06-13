# -*- coding: utf-8 -*-

class Config(object):
    """ Setting up all configuration for Flask app in my_website.py"""
    
    # Setting up url to the database. set track_modify = False to reduce overhead
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Phihung94@localhost:5432/CS_Projects_Data'
    SQLALCHEMY_TRACK_MODIFICATION = False