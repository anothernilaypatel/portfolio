# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 01:18:17 2024

@author: Nilay Patel

TODO: GET BASIC WEBSITE SET UP (home page) AND GIT

"""
import flask
app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return flask.render_template("home.html")   

if __name__ == "__main__":
    app.run(host="localhost", port=5000)