#!/usr/bin/env python3 
#-*- coding: utf8 -*-
"""Route definitions"""

from app import app

@app.route("/")
def index():
    return "Hello, world!"


@app.route("/about")
def about ():
    me = {
        "first_name": "Eric",
        "last_name": "Babin",
        "hobbies": "Broadcasting"
    }
    return me
